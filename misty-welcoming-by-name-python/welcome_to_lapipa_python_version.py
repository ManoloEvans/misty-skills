from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters
import json

misty = Robot(ip = "192.168.128.86")

misty.start_face_recognition()


def registerFaceDetection ():
    # Create Register Face Detection here in python.

def _FaceDetect(data):

    face_detected = data.PropertyTestResults[0].PropertyParent.Label

    if face_detected == "unknown person":
        #misty.Debug(json.stringify(data));
        #misty.Set("faceInFOV", true, false);
        misty.change_led(148, 0, 211)
        misty.display_image("e_Joy2.jpg")
        misty.speak("Hello human, welcome to La Pipa! What's your name?")
        misty.pause_audio(3500) # Waiting 3.5s since it doesn't wait for speak to end
        misty.pause_skill(3500)

        misty.AddReturnProperty("VoiceRecord", "Filename")
        misty.AddReturnProperty("VoiceRecord", "Success")
        misty.AddReturnProperty("VoiceRecord", "ErrorCode")
        misty.AddReturnProperty("VoiceRecord", "ErrorMessage")
        misty.RegisterEvent("VoiceRecord", "VoiceRecord", 10, false)

        misty.debug("Recording audio..")
        misty.CaptureSpeech(false, true, 10000, 5000, null)

        misty.RegisterTimerEvent("timeoutToNormal", 5000, false)
def _TimeoutToNormal():
    # Create _timeoutToNormal here in python.

def _VoiceRecord():
    # Create Voice record function here in python.

def _GetAudioFile(data):

    base64 = data.Result.Base64
    apikey = APIKEY

    misty.SendExternalRequest(
        "POST",
        "https://speech.googleapis.com/v1p1beta1/speech:recognize?key=" + apikey,
        None,
        None,
        json.dumps({"FileName": file_name, "DataAsByteArrayString": new_string,
                    "ImmediatelyApply": True, "OverwriteExisting": True})

#            {
#            audio": {"content": base64
#            } ,
#            "config": {
#                "enableAutomaticPunctuation": True,
#                "encoding": "LINEAR16",
#                "languageCode": "es-ES",
#                "model": "command_and_search"
#            }

#        )
    )

def _SendExternalRequest():
    # Create SendExternalRequest here in python.



