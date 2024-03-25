var staticCacheName = 'pmv-attendance-v1';

self.addEventListener('install', function(event) {
event.waitUntil(
	caches.open(staticCacheName).then(function(cache) {
	return cache.addAll([
		'/home/',
	]);
	})
);
});

self.addEventListener('fetch', function(event) {
var requestUrl = new URL(event.request.url);
	if (requestUrl.origin === location.origin) {
		if (requestUrl.pathname === '/home') {
			event.respondWith(caches.match('/home'));
			return;
		}
	}
	event.respondWith(
		caches.match(event.request).then(function(response) {
			return response || fetch(event.request);
		})
	);
});

self.addEventListener('push', function(event) {
	var body;
	if (event.data) {
		body = event.data.text();
	} else {
		body = 'Push message no payload';
	}
	var options = {
		body: body,
		icon: 'images/icon.png',
		badge: 'images/badge.png'
	};
	event.waitUntil(self.registration.showNotification('Push Notification', options));
});