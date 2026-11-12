#!/bin/bash
# Doppelklick (Mac): startet das Spiel lokal und öffnet den Browser
cd "$(dirname "$0")"
(sleep 4; open http://localhost:3000) &
npx serve . -l 3000
