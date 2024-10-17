odoo.define('area_in_country.map_link', function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.MapLink = publicWidget.Widget.extend({
        start: function() {
            console.log('MapLink Widget Started');  // Dòng này giúp kiểm tra
            var location = this.$el.data('location'); // Lấy giá trị location từ data attribute
            var mapLink = document.getElementById('map_link');
            if (mapLink) {
                mapLink.href = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(location);
            }
        },
    });
});
