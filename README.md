# Jaxx

Where's your head at?

## Prerequisites

- `sudo apt-get install python-systemd`
- `pip install redis`
- You also need `servod` for initio compatibility

## Message Spec

Format: \<channel> "message"

**Inputs**

* \<jaxx> "\<pan_angle>,\<pitch_angle>"
  * Points the head at the specified pan and pitch angles
  * Note that 0,0 is dead ahead
  * Details to follow on exact range capability

**Outputs**

None