# Smart Irrigation System 🌱💧

An IoT-based automated plant watering system that combines a Flutter mobile application with Raspberry Pi hardware to provide intelligent irrigation control. The system supports multiple watering modes, real-time sensor monitoring, and multi-language support (French/Arabic).

## 🎯 Features

### Mobile Application
- **User Authentication**: Secure login, registration, and password reset via Firebase
- **Multi-language Support**: French and Arabic interfaces
- **Multiple Irrigation Modes**:
  - **Manual Mode**: Instant watering control
  - **Automatic Mode**: Soil moisture-based automatic watering
  - **Programmed Mode**: Scheduled watering by day and time
- **Real-time Monitoring**: Live temperature, humidity, and soil moisture data
- **User Profiles**: Personalized user settings and preferences
- **Push Notifications**: Alerts and system updates
- **Modern UI**: Curved navigation bar, custom icons, and smooth animations

### Hardware System
- **Sensor Integration**:
  - DHT22 temperature and humidity sensor
  - Soil moisture sensor (via Arduino)
  - Water level monitoring
- **Actuator Control**: GPIO-based water pump control
- **Firebase Integration**: Real-time data synchronization

## 🏗️ Architecture

```
smart-irrigation-system/
├── mobile-app/                 # Flutter application
│   ├── lib/
│   │   ├── authentication/    # Login, register, password reset
│   │   ├── home/              # Main dashboard and navigation
│   │   ├── irrigation/        # Watering modes and controls
│   │   ├── sensors/           # Sensor data display
│   │   ├── profile/           # User profile management
│   │   ├── notifications/     # Push notification service
│   │   └── utils/             # Shared utilities and widgets
│   ├── assets/                # Images, fonts, icons
│   ├── android/               # Android configuration
│   ├── ios/                   # iOS configuration
│   └── pubspec.yaml           # Dependencies
├── hardware/                  # Raspberry Pi code
│   ├── sensors.py             # Sensor reading functions
│   ├── modes.py               # Irrigation mode logic
│   ├── firestore_setup.py     # Firebase configuration
│   ├── getters.py             # Data retrieval
│   ├── dictionary.py         # Translation utilities
│   └── serviceAccountKey.json # Firebase credentials (⚠️ DO NOT COMMIT)
├── docs/                      # Documentation
│   ├── installation-guide.pdf
│   └── user-manual.pdf
└── README.md
```

## 🛠️ Tech Stack

### Mobile App
- **Framework**: Flutter (Dart SDK >=2.12.0 <3.0.0)
- **Backend**: Firebase (Auth, Firestore, Analytics)
- **State Management**: Provider
- **Key Libraries**:
  - `curved_navigation_bar` - Navigation UI
  - `weather_icons` - Weather-related icons
  - `rolling_switch` - Custom toggle switches
  - `http` - HTTP requests
  - `flutter_local_notifications` - Push notifications
  - `lottie` - Animations

### Hardware
- **Platform**: Raspberry Pi 4
- **Language**: Python 3
- **Sensors**: DHT22, Soil Moisture Sensor
- **Communication**: Serial (UART), GPIO
- **Cloud**: Firebase Admin SDK

## 👥 Team

This project was developed by a team of 6 students in 2021-2022:
- **Asma Sebah & Yasmine Belmellat** - UI/UX design and home screens
- **Salma Taib & Selma Zerrouki** - Flutter App developpment
- **Soundos Benni & Hind Ledra** - Hardware integration and testing

## 📄 License

This project is provided as-is for educational purposes.


## ⚠️ Security Notes

- **NEVER commit** `serviceAccountKey.json` or any Firebase credentials
- Add `serviceAccountKey.json` to `.gitignore`
- Use environment variables for sensitive configuration
- Regularly update dependencies for security patches

## 📞 Support

For installation guides and user manuals, refer to the PDF documentation in the `docs/` folder.

## 🎥 Demo Videos

Demo videos showcasing the system functionality are available. These demonstrate:
- Mobile app navigation and features
- Hardware setup and sensor readings
- All irrigation modes in action
- Real-time data synchronization

*Note: Demo videos should be uploaded to a video hosting platform (YouTube, Vimeo) and linked in this README for better accessibility.*
