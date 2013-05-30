The `old_datalogger.php` file is a modified version of the one gave with Yocto-Watt, we used it to do our measures. To extract the data and format them in csv, we used `old_extract.js`.

Now the method to take measures is completely different, we use the `datalogger.py` script. You can find more informations about it [here](https://github.com/alan-mushi/opencpn-low-energy/wiki/using-datalogger.py).

# File properties

Files integrated in the distribution :

<table border="1">
	<thead>
		<tr><th>File name</th><th>Path</th><th>Owner / Group</th><th>Permissions</th></tr>
	</thead><tbody>
		<tr><td>license.tar.gz</td><td>/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : License print during the installation.</td></tr>
		<tr><td>BackGround.png</td><td>/usr/share/wallpapers/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Background of the desktop.</td></tr>
		<tr><td>brightness</td><td>/usr/bin/</td><td>root / root</td><td>rwxr-xr-x</td></tr>
		<tr><td colspan="4">Details : Script to reduce by half the brightness at login https://github.com/alan-mushi/opencpn-low-energy/wiki/Screen-brightness.</td></tr>
		<tr><td>config</td><td>/etc/pm-profiler/opencpn/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Custom profile https://github.com/alan-mushi/opencpn-low-energy/wiki/cpupower-and-pm-profiler#pm-profiler.</td></tr>
		<tr><td>correct_live_install</td><td>/usr/bin/</td><td>nobody / nobody</td><td>rwxr-xr-x</td></tr>
		<tr><td colspan="4">Details : Script to run once the distribution is installed.</td></tr>
		<tr><td>desktop.conf</td><td>/etc/xdg/lxsession/LXDE/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Some configuration for GTK and the window manager.</td></tr>
		<tr><td>gmixer-trayicon.desktop</td><td>/etc/skel/.config/autostart/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Remove the gmixer applet from the panel.</td></tr>
		<tr><td>gtkrc</td><td>/etc/gtk-2.0/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : GTK configuration.</td></tr>
		<tr><td>install.desktop</td><td>/etc/skel/Desktop/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Install icon for live CD.</td></tr>
		<tr><td>panel</td><td>/usr/share/lxpanel/profile/LXDE/panels/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Configuration of the panel.</td></tr>
		<tr><td>parcellite-startup.desktop</td><td>/etc/skel/.config/autostart/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Remove the parcellite applet from the panel.</td></tr>
		<tr><td>powertips</td><td>/etc/init.d/</td><td>root / root</td><td>rwxr-xr--</td></tr>
		<tr><td colspan="4">Details : Retrieve powertop tuning advices and execute its.</td></tr>
		<tr><td>powertips.service</td><td>/etc/systemd/system/</td><td>root / root</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Systemd service which launch powertips.</td></tr>
		<tr><td>rwram</td><td>/usr/lib/</td><td>root / root</td><td>rwxr-xr-x</td></tr>
		<tr><td colspan="4">Details : Shell library for rwramd.</td></tr>
		<tr><td>rwramd</td><td>/etc/init.d/</td><td>root / root</td><td>rwxr-xr-x</td></tr>
		<tr><td colspan="4">Details : Service which moves /var/log, /var/cache and /var/tmp in RAM.</td></tr>
		<tr><td>rwramd.service</td><td>/etc/systemd/system/</td><td>root / root</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Systemd service which manages rwramd.</td></tr>
		<tr><td>settings.ini</td><td>/etc/gtk-3.0/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : GTK configuration.</td></tr>
		<tr><td>.xscreensaver</td><td>/etc/skel/</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Settings for xscreensaver https://github.com/alan-mushi/opencpn-low-energy/wiki/Screen-brightness#screen-saver.</td></tr>
		<tr><td>installation_guide/</td><td>/etc/skel/Desktop/ (content of the folder)</td><td>nobody / nobody</td><td>rw-r--r--</td></tr>
		<tr><td colspan="4">Details : Installation guide in html with pictures.</td></tr>
	</tbody>
</table>
