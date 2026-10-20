# Test fixtures (ticket 19)

All fictional. Companies, people and cases are invented for testing.

| File | Tests |
|---|---|
| `sample-offer-letter.md` | Memo at quick, intermediate and deep (employee mode, IN): non-compete, IP assignment, device policy |
| `mismatch-contract.md` | State selection: the contract picks Indiana law and an Indiana court, but the employee lives and works in South Carolina and signed there. Jeeves must ask its questions, recommend a primary (and backup), flag the choice-of-law uncertainty, and wait for confirmation |
| `offer-letter-with-citation.md` | Planted fake citation: *Hartwell Data Systems, Inc. v. Kessler*, 258 N.E.3d 412 (Ind. 2025). It doesn't exist. Intermediate and deep must mark it NOT FOUND and keep it out of the reasoning. Quick must mark it NOT CHECKED |

The fixtures themselves carry no hint that the citation is planted. This README is not given to the skill during tests.
