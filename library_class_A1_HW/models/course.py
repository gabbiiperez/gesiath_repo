from odoo import models, fields # type: ignore


class Course(models.Model):
    _name = "course"
    _description = "Odoo's Course"

    name = fields.Char(string="Name of the course", required=True)
    duration = fields.Integer(string="Duration of the course")
    description = fields.Char(string="Description of the course")

    def create_course(self):
        course_id = self.env["course"].create({"name":"Basic Python"})
        print(course_id.id)
    
    def search_course(self):
        courses = self.env["course"].search([])
        for course in courses:
            print(course.name)

    def write_course(self):
        course_id = self.env["course"].search([("name", "=", "Basic Python")], limit=1)
        if course_id:
            course_id.write({"name":"Advanced Python"})

    def unlink_course(self):
        course_id = self.env["course"].search([("name", "=", "Advanced Python")], limit=1)
        if course_id:
            course_id.unlink()
