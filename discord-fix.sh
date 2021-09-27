# Runs VLC as a mirror to a screen to workaround issue on discord
# where sharing only one screen isn't possible
vlc \
    --no-video-deco \
    --no-embedded-video \
    --screen-fps=30 \
    --screen-top=0 \
    --screen-left=0 \
    --screen-width=2560 \
    --screen-height=1440 \
    screen://
