# The Passport Page of a Country That Isn't There — Republic of Meridia

[![Passport](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![Rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/tranquilnaturevista-code/passport-nowhere/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![Reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/tranquilnaturevista-code/passport-nowhere/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

This entry is one open passport spread for a country that does not
exist: the **Republic of Meridia**, a small tidal island nation in the
South Atlantic, capital Port Lumen, founded 1847. Its motto is "One
island, one tide" — and that is not decoration, it is the document's
telling detail.

The `main.py` script does the whole delivery job — it copies the
finished `entry.png` image, byte for byte, to `/output/entry.png`, so
the spread that gets judged is exactly the spread that was laid out,
with no re-rendering or recompression in between.

## The spread

- **Left page — the data page:** the Meridian coat of arms (a
  lighthouse over two waves, one star), the holder Mara Ellin Voss,
  born 14 April 1991 in Port Lumen, passport MD2048173, issued
  12 March 2024 and valid until 12 March 2034, with a machine-readable
  zone whose check digits are computed to the ICAO TD3 format.
- **Right page — visas and stamps:** a single-entry tourist visa from
  the neighbouring Kingdom of Vostra (issued 15 May 2024, valid
  1–30 June 2024, fee 40 crowns, employment not permitted), and a
  travel history that agrees with it: out of Port Lumen on 3 June
  2024, into Vostra the same day, home on 11 June 2024, then a
  second trip to Caldara, 2–19 September 2025. No stamp predates the
  passport, and every arrival has its matching departure.
- **The telling detail:** a printed condition of entry — the causeway
  to Meridia is passable only at low tide, and arrivals later than
  two hours after high water are refused and returned on the next
  ebb. That is what kind of place Meridia is: an island you can only
  reach when the sea lets you.

## How it works

Run `python3 main.py` and the script copies `entry.png` from this
folder into the output folder (the `MAKEFUN_OUTPUT_DIR` environment
variable, or `/output` when that is not set), creating the folder if
it does not exist yet.

## Verification

After copying, the script checks that the copy is exactly the same
size in bytes as the original and stops with an error if the two
sizes differ. Comparing the SHA-256 hash of the output against the
original gives the same guarantee: the two files should match
exactly.
