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

None