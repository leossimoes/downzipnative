# DownzipNative

DownzipNative is a Windows-based background program designed to serve as a native message host for the Chrome extension "Downzip." It seamlessly integrates with the `chrome.downloads` API to automatically unpack downloaded archives based on user preferences set in the extension's popup.

## Installation

1. Download the latest release installer from the [Releases](https://github.com/leossimoes/downzipnative/releases) section.

2. Run the installer (`DownzipNativeInstaller.exe`) to set up DownzipNative on your Windows system.

3. Ensure that the "Downzip" Chrome extension is installed and active.

4. No manual program launch is required. DownzipNative works silently in the background.

## Usage

1. **Chrome Extension**: Make sure the "Downzip" Chrome extension is installed and configured.

2. **Download Archives**: When files are downloaded through the Chrome browser, the extension captures the download event and communicates with the service worker.

3. **Native Message**: The service worker sends a native message to `DownzipNative`, containing information about the downloaded archive, such as file path and folder location.

4. **Unpacking**: `DownzipNative` processes the message, creates the necessary folder, unpacks the archive into it, and optionally deletes the original archive based on user preferences set in the extension's popup.

## Technical Details

- **Platform**: Windows
- **Language**: Python
- **Compiler**: PyInstaller
- **Environment Manager**: Miniconda
- **Chrome Extension Name**: Downzip
- **Executable Name**: DownzipNative
- **Chrome API Integration**: Utilizes the `chrome.downloads` API events to capture download information.
- **Service Worker Communication**: The extension leverages a service worker to send native messages to the `DownzipNative` Python script. This ensures efficient and non-blocking communication between the browser and the native message host.

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Author

Léo Simões

---