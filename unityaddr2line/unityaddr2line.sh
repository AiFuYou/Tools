#!/bin/bash

cmd="/xxxx/Android/sdk/android-ndk-r16b/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin/arm-linux-androideabi-addr2line -C -f -e  /Applications/Unity/PlaybackEngines/AndroidPlayer/Variations/il2cpp/Release/Symbols/armeabi-v7a/libunity.sym.so "

for arg in $@
do
#echo $arg
$cmd $arg
done
