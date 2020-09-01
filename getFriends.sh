#!/bin/bash
curl --request GET --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=Bot36374925' --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAAN7aHAEAAAAAwbhe2d8L7cVbG5ABP0MBObZjj3w%3Dng6FOd0DaIlM9A4Zcqy9PSndwENpndpw1B3qVcbcM9ZNIqE2O5' > users_ids.txt
sed 's/.*\[\([^]]*\)].*/\1/' users_ids.txt > ids.txt
