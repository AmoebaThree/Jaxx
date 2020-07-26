# Jaxx

Where's your head at?

## Message Spec

Format: \<channel> "message"

**Inputs**

* \<jaxx> "\<pan_angle>,\<pitch_angle>"
  * Points the head at the specified pan and pitch angles
  * Note that 0,10 is dead ahead, but you can just publish `jaxx 0` to get there
  * Pan angle range: +- 80; Pitch angle range: +80 to -25; these are enforced in the code

**Outputs**

* \<jaxx.head> "\<pan_angle>,\<pitch_angle>"
  * Outputs the angle the Jaxx head has been set to
  * This includes any enforcements made, so may not be the same as the input
  * If `jaxx 0` is provided then it will return you the actual dead ahead angle