# DEADFACE CTF 2022
## Dreaming of You

> Created by: RP-01?
>
> Someone doesn't understand networking traffic. Now I know their deepest crush. Can you find the flag from the PCAP file? Submit the flag as flag{text}.
>
> [Download File](DeadfacePcap.pcapng)
>
> SHA1: 1c99dee5307143e7dad0f0a19e58ad431eb5b8ce

## Summary

strings + grep to find flag

## Detailed Solution

`strings DeadfacePcap.pcapng | grep flag` easily finds the flag.

Flag: `flag{longing_for_nancy}`

If you wanted to do this through Wireshark, check Statistics -> Protocol Hierarchy. Lots of telnet, so right click and filter. There are two telnet streams, index 0 and 4 (you may need to apply the Stream index column to see this). Follow the stream for index 4 and at the bottom is the flag.