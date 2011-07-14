
A small Django application to detect mobile browsers.

Provides a template context processor so your templates can always
know if the user happens to be viewing your site from a mobile
browser. The detection is crude, and user agents are always changing.

I'm just creating this project for a simple app I have on a personal
project that doesn't really matter if we get the detection right or wrong.
I'm mostly just concerned about finding android or iphone.

By Default, there will be a cookie set called "use_mobile" and the
value will be true or false depending on whether you want the mobile
view or desktop view. If you want to change the cookie name, change the
MOBILE_COOKIE_NAME setting.