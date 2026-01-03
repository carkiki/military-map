# Offline Map Guide

This guide explains how to download and use the military bases map offline on any device.

## Quick Start

You have **TWO offline versions** to choose from:

### Option 1: Semi-Offline (Best Visual Quality)
**File:** `military_bases_offline.html`
- Uses OpenStreetMap tiles (requires internet for map background)
- All base data and functionality works offline
- Best visual appearance
- File size: ~18 KB

### Option 2: 100% Offline (No Internet Needed)
**File:** `military_bases_100percent_offline.html`
- Works completely offline with custom canvas-based map
- No internet required at all
- Interactive pan and zoom
- File size: ~27 KB

## How to Download and Use

### Method 1: Save from Browser (Easiest)

1. **Start the Flask app** (if not already running):
   ```bash
   cd /home/user/military-map
   python app.py
   ```

2. **Open browser** and download the file:
   - For semi-offline: http://localhost:5000/static/../military_bases_offline.html
   - For 100% offline: http://localhost:5000/static/../military_bases_100percent_offline.html

3. **Right-click** on the page → **Save As** → Choose "Webpage, Complete"

4. **Transfer to any device**:
   - Email to yourself
   - Copy to USB drive
   - AirDrop/Share to phone or tablet
   - Upload to cloud storage (Dropbox, Google Drive, etc.)

### Method 2: Direct File Copy

Simply copy either HTML file from the project directory:
```bash
/home/user/military-map/military_bases_offline.html
/home/user/military-map/military_bases_100percent_offline.html
```

And open it in any web browser on any device!

## Using on Different Devices

### Desktop/Laptop (Windows, Mac, Linux)
1. Double-click the HTML file
2. It will open in your default browser
3. Works in: Chrome, Firefox, Safari, Edge

### iPhone/iPad
1. Save the HTML file to Files app
2. Tap to open in Safari
3. Optional: Add to Home Screen for app-like experience
   - Tap Share button → "Add to Home Screen"

### Android Phone/Tablet
1. Save the HTML file to Downloads
2. Open with Chrome, Firefox, or any browser
3. Optional: Add to Home Screen
   - Menu → "Add to Home Screen"

### Kindle/E-Reader
1. Transfer HTML file via USB
2. Open with built-in browser (Experimental Browser on Kindle)

## Features Available Offline

### Semi-Offline Version (`military_bases_offline.html`)
- ✅ Interactive map with real map tiles (needs internet)
- ✅ 25 military base locations
- ✅ Click markers for detailed information
- ✅ Search bases by name, state, or branch
- ✅ Color-coded by military branch
- ✅ Exclusion zones (10km radius)
- ✅ Zoom and pan controls
- ✅ Legend and statistics

### 100% Offline Version (`military_bases_100percent_offline.html`)
- ✅ Custom canvas-based map (no internet needed)
- ✅ All 25 military base locations
- ✅ Click bases for information
- ✅ Search functionality
- ✅ Drag to pan
- ✅ Scroll/pinch to zoom
- ✅ Zoom buttons (+/- and reset)
- ✅ Touch-friendly for mobile
- ✅ Works in airplane mode!

## Sharing the Maps

### Share via Email
1. Attach the HTML file to email
2. Recipients can download and open
3. Works on any device with a browser

### Share via Cloud
1. Upload to Google Drive, Dropbox, OneDrive, etc.
2. Share the link
3. Others can download and open offline

### Share via QR Code
1. Upload file to a file-sharing service
2. Generate QR code for the download link
3. Scan QR code with phone camera

## Tips for Best Experience

### For Semi-Offline Version
- Open once while connected to internet (map tiles will cache)
- Base data always works offline
- Better for presentations when internet is available

### For 100% Offline Version
- Perfect for areas with no internet
- Great for planes, remote locations, etc.
- Lighter weight, faster loading
- Touch-friendly interface

### General Tips
1. **Mobile Use**: Works best in landscape orientation
2. **Search**: Type any part of base name, state, or branch
3. **Zoom**: Use controls or mouse wheel (desktop) / pinch (mobile)
4. **Pan**: Click and drag (desktop) / swipe (mobile)
5. **Reset View**: Click home button (⌂) to reset to original view

## Troubleshooting

### File Won't Open
- Make sure you have a web browser installed
- Try right-click → "Open With" → Choose browser
- On mobile: Move file to accessible location (Downloads/Files)

### Map Not Showing (Semi-Offline Version)
- This version needs internet for map background
- Use the 100% offline version instead
- Or connect to internet once to load tiles

### Slow Performance
- Close other browser tabs
- Try the semi-offline version (it's lighter)
- Reduce zoom level

### Can't See Bases on Mobile
- Rotate device to landscape
- Use zoom controls
- Tap on base list to jump to location

## File Specifications

| Version | File Size | Internet Required | Map Quality | Best For |
|---------|-----------|-------------------|-------------|----------|
| Semi-Offline | ~18 KB | For map tiles | High quality | Regular use |
| 100% Offline | ~27 KB | None | Simple/functional | No internet |

## Security & Privacy

- ✅ No external servers (except map tiles in semi-offline)
- ✅ No tracking or analytics
- ✅ All data is public information
- ✅ Works completely locally
- ✅ No data collection

## Updating the Maps

If new bases are added to the project:
1. The HTML files are static snapshots
2. Re-download/copy the updated HTML files
3. Replace old files with new ones

## Advanced: Creating Your Own Offline Map

You can modify the HTML files:
1. Open in text editor (Notepad++, VSCode, etc.)
2. Find the `militaryBases` array in the `<script>` section
3. Add/remove/edit bases
4. Save and reopen in browser

## Support

For issues or questions:
- Check the main README.md file
- Review the Flask app source code in app.py
- All military base data is in data/military_bases.json

---

**Enjoy your offline military bases map! 🗺️**
