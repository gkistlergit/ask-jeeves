# Using Jeeves from the phone

Two routes (ticket 31). Use **route 1** when the Mac is on and you want the full skill. Use **route 2** for a quick memo when the Mac is off or out of reach.

| | Route 1: full Jeeves, Mac driven from the phone | Route 2: chat Jeeves in the Claude app |
|---|---|---|
| Depths | quick, intermediate, deep | quick only |
| States | built-in files, state cards, any state via web research | built-in files and state cards only |
| Location for the attorney finder | typed, Home or Aiken. Live location reads the **Mac** | typed, Home or Aiken. No live location |
| Attorney finder | yes | only if the chat has web search on |
| Run log and refresh queue | yes | no |
| PDFs | scans and encrypted PDFs read on the Mac | what the chat can read; otherwise paste the text |

## Route 1: full Jeeves on the Mac, driven from the phone

The session runs on the Mac, so the statute library, the scripts, the run log and the refresh queue all work. The phone is only a window into it.

1. On the Mac, start a Remote Control session and keep the Mac awake while it runs:
   ```bash
   cd ~ && caffeinate -i claude remote-control --name jeeves
   ```
   In the desktop app you can turn on Remote Control for a Code session instead.
2. On the phone, open the Claude app, go to **Code**, and open the session named `jeeves`. claude.ai/code in the phone's browser works too.
3. Type `/ask-jeeves`, then answer the questions as usual.
4. **Location:** when the attorney finder offers *My live location*, it means the Mac's location. Away from the Mac, pick *Type a ZIP* and type the ZIP or the city your phone shows.
5. **Documents:** paste the text, or save the file to iCloud Drive on the phone and give Jeeves its path on the Mac (`~/Library/Mobile Documents/com~apple~CloudDocs/<file>`).

Stop the session with Ctrl-C on the Mac when you're done. `claude remote-control --continue` reattaches to the last one from the same folder within about 4 hours.

## Route 2: chat Jeeves as a claude.ai skill

claude-global-settings builds the upload zip from the pinned commit (`claudeAi: true` on the `ask-jeeves` skill package):

```bash
~/Developer/claude-global-settings/bin/harness build-zips
```

That writes `~/Developer/claude-global-settings/build/claude-ai/ask-jeeves.zip`. It holds only the skill folder, `ask-jeeves/`: SKILL.md, the references, the state cards, the memo template and the Mac-only scripts, which chat Jeeves doesn't run. There's no `Sources/`, run log, refresh queue or input document in it.

1. On claude.ai (web), open **Settings → Capabilities**, turn on code execution if it's off, and upload `ask-jeeves.zip` under **Skills**. Re-upload after each pin bump that changes the skill.
2. In the Claude phone app, start a chat and ask for "ask-jeeves" by name. The skill only runs when named.
3. Jeeves says it's chat Jeeves and runs a quick memo. For the attorney finder, turn on web search in that chat first.
