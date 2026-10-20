// Jeeves Location: prints "City|ZIP" for this Mac's current location, then quits.
// Coordinates are never printed or saved. macOS shows its own permission prompt for this
// app; Apple's geocoder turns the location fix into a city and ZIP.
// Output on failure: DENIED, FAILED, GEOCODE_FAILED or TIMEOUT.
import AppKit
import CoreLocation

final class Locator: NSObject, NSApplicationDelegate, CLLocationManagerDelegate {
    let manager = CLLocationManager()

    func applicationDidFinishLaunching(_ note: Notification) {
        NSApp.activate(ignoringOtherApps: true)
        manager.delegate = self
        manager.desiredAccuracy = kCLLocationAccuracyHundredMeters
        DispatchQueue.main.asyncAfter(deadline: .now() + 90) { self.finish("TIMEOUT", code: 7) }
        handle(manager.authorizationStatus, firstLook: true)
    }

    // The initial status callback doesn't always fire on macOS, so launch checks the status itself.
    func handle(_ status: CLAuthorizationStatus, firstLook: Bool = false) {
        switch status {
        case .notDetermined:
            if firstLook { manager.requestWhenInUseAuthorization() }
        case .denied, .restricted:
            finish("DENIED", code: 6)
        default:
            manager.requestLocation()
        }
    }

    func locationManagerDidChangeAuthorization(_ m: CLLocationManager) {
        handle(m.authorizationStatus)
    }

    func locationManager(_ m: CLLocationManager, didUpdateLocations locs: [CLLocation]) {
        guard let loc = locs.last else { return }
        CLGeocoder().reverseGeocodeLocation(loc) { marks, _ in
            guard let p = marks?.first else { self.finish("GEOCODE_FAILED", code: 5); return }
            self.finish("\(p.locality ?? "")|\(p.postalCode ?? "")", code: 0)
        }
    }

    // While the prompt is still open, locationd reports "denied"; keep waiting for the answer.
    func locationManager(_ m: CLLocationManager, didFailWithError e: Error) {
        if (e as? CLError)?.code == .locationUnknown || m.authorizationStatus == .notDetermined { return }
        finish(m.authorizationStatus == .denied ? "DENIED" : "FAILED", code: 6)
    }

    func finish(_ line: String, code: Int32) {
        print(line)
        fflush(stdout)
        exit(code)
    }
}

let app = NSApplication.shared
app.setActivationPolicy(.accessory)
let delegate = Locator()
app.delegate = delegate
app.run()
