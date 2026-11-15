from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Chris',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
        
    def test_name_is_invalid(self):
        """Testing empty fields"""
        
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is not valid")
        
        
    def test_email_is_invalid(self):
            """Testing empty fields"""
            
            form = CollaborateForm({
                'name': 'Chris',
                'email': '',
                'message': 'Hello!'
            })
            self.assertFalse(form.is_valid(), msg="Form is not valid")
            
            
    def test_message_is_invalid(self):
            """Testing empty fields"""
            
            form = CollaborateForm({
                'name': 'Chris',
                'email': 'test@test.com',
                'message': ''
            })
            self.assertFalse(form.is_valid(), msg="Form is not valid")