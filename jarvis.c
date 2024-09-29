#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <windows.h>
#include <sapi.h>
#include <speechapi_cxx.h>

using namespace std;
using namespace Microsoft::CognitiveServices::Speech;

void speak(const string& audio) {
    ISpVoice* pVoice = NULL;
    CoInitialize(NULL);
    if (FAILED(CoCreateInstance(CLSID_SpVoice, NULL, CLSCTX_ALL, IID_ISpVoice, (void**)&pVoice))) {
        return;
    }
    pVoice->Speak(std::wstring(audio.begin(), audio.end()).c_str(), SPF_IS_XML, NULL);
    pVoice->Release();
    CoUninitialize();
}

string takeCommand() {
    // Placeholder for speech recognition logic
    // This requires a speech recognition library or API
    // For now, we will return a dummy command
    return "open notepad"; // Simulating user input
}

void wish() {
    time_t now = time(0);
    tm* localtm = localtime(&now);
    int hour = localtm->tm_hour;

    if (hour >= 0 && hour < 12) {
        speak("Good Morning");
    } else if (hour >= 12 && hour < 18) {
        speak("Good Afternoon");
    } else {
        speak("Good Night");
    }

    speak("Sir I am Jack How can I help you sir");
}

int main() {
    wish();
    string query = takeCommand();

    if (query.find("open notepad") != string::npos) {
        system("start notepad");
    } else if (query.find("open cmd") != string::npos) {
        system("start cmd");
    }

    return 0;
}

