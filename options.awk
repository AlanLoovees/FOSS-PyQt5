{
    if ($1=="ro"||$2=="ro"||$3=="ro"||$4=="ro")
    {
        print "Read-Only\n"
        print "This option tells the kernel to mount the root  filesystem  as read-only so that filesystem consistency check programs (fsck) can do their work on a quiescent filesystem.\n\n"
    }
    if ($1=="quiet"||$2=="quiet"||$3=="quiet"||$4=="quiet")
    {
        print "Quiet\n"
        print "This option tells the kernel to NOT produce any output. If you boot without this option, you'll see lots of kernel messages such as drivers/modules activations, filesystem checks and errors.\n\n"
    }
    if ($1=="splash"||$2=="splash"||$3=="splash"||$4=="splash")
    {
        print "Splash\n"
        print "This option is used to start a loading screen while all the core parts of the system are loaded in the background\n\n"
    }
    if ($1=="vt.handoff=1"||$2=="vt.handoff=1"||$3=="vt.handoff=1"||$4=="vt.handoff=1")
    {
        print "vt.handoff\n"
        print "This options is unique to Ubuntu. Its purpose is to allow the kernel to maintain the current contents of video memory on a virtual terminal. So, when the operating system is booting up, when it moves past the boot loader, vt.handoff allows showing of an aubergine background, with Plymouth displaying a logo and progress indicator bar on top of this. Once the display manager comes up, it smoothly replaces this with a login prompt.\n\n"
    }
    if ($1=="nomodeset"||$2=="nomodeset"||$3=="nomodeset"||$4=="nomodeset")
    {
        print "nomodeset\n"
        print "Nomodeset parameter instructs the kernel to not load video drivers and use BIOS modes instead until the graphics driver is loaded\n\n"
    }
}