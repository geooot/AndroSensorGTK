# AndroSensorGTK
A Blender plugin that uses phone gyroscope data as keyframes

## Get it running
### Steps on your phone
1. Install the [AndroSensor app (free) ](https://play.google.com/store/apps/details?id=com.fivasim.androsensor&hl=en) on your Android Phone
2. Open the AndroSensor app and tweak the apps settings to the following:
  1. *Update Interval* -> Very Fast
  2. *Lock orientation* -> True
  3. *Keep screen on* -> True
  4. *Active Sensors* -> Only `GYROSCOPE`
  5. *CSV file format* -> `;`
  6. *Recording Interval* -> Activate `fast` mode and set it to `0.100~0.200 seconds`
  7. Press the arrow button on the top to open the toolbar menu
  8. Press the red `record` button to start recording keyframes

*Step 1-3 is for convenience only, you might aswell choose the settings you prefer.*

### Steps in Blender
1. Just install the plugin as you install any other plugin:
  1. Download the [py file (direct link)](https://raw.githubusercontent.com/fschoenfeldt/AndroSensorGTK/master/AndroSensorGTK.py)
  2. In Blender, go to `Edit -> Preferences -> Addons -> Install...`
  3. Choose the py file
2. In the Objects panel, scroll down to "AndroSensor GTK"
3. Choose the .csv file created by the Android app
4. Click `add keyframes`

## Troubleshooting
**Python Error `too many values to unpack`**

You chose the wrong sensors on the Android app, just select `GYROSCOPE` there. *AndroSensorGTK does not work with accelerometer (or any other sensors than the gyroscope)!*

**Can I use other sensors with this add-on?**

AndroSensorGTK does not work with accelerometer (or any other sensors than the gyroscope)!

**I have a feature request or issues**

Please contribute!

## Contributors
- [@fschoenfeldt](https://github.com/fschoenfeldt)
- [@geooot](https://github.com/geooot)
