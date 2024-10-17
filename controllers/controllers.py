from odoo import http

class AreasInCountry(http.Controller):
    @http.route('/areas_in_country', auth='public', website=True)
    def areas(self, **kwargs):
        # Truyền biến vào template (nếu cần)
        return http.request.render('areas_in_country_template', {
            'areas_name': 'Sample Area'
        })
class MapController(http.Controller):

    @http.route('/map/show', type='http', auth='public', website=True)
    def show_map(self, **kwargs):
        # Truy vấn dữ liệu từ model areas_in_country
        locations = request.env['areas_in_country'].search([])  # Sử dụng model areas_in_country
        return request.render('areas_in_country.map_template', {
            'locations': locations,
        })