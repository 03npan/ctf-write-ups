# UMDCTF 2022
## Renzik's Case

> My friend deleted important documents off of my flash drive, can you help me find them?
>
> Note: The flag can be submitted with or without the hiphen ex. UMDCTF-{flag} or UMDCTF{}
>
> [https://drive.google.com/file/d/1VmUyHJqU11E0UE7OYTPYV3U2yVh2qL5g/view?usp=sharing](https://drive.google.com/file/d/1VmUyHJqU11E0UE7OYTPYV3U2yVh2qL5g/view?usp=sharing)
>
> **Author**: matlac

Category: *forensics*

## Summary

Use Disk Drill to recover deleted files and find the flag.

## Detailed Solution

Install [Disk Drill](https://www.cleverfiles.com/usb-flash-drive-recovery.html). Choose `Attach disk image` and select `usb.img` provided in the ZIP file. Select `Search for lost data` on the USB.

In the `Reconstructed labeled` category, there is one PNG file: `most_secure_password`. Clicking on it gives us the flag.

![flag.png](https://github.com/03npan/ctf-write-ups/blob/main/umdctf_2022/renziks_case/flag.png)