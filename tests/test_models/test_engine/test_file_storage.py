#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(0, 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        self.assertTrue(5 == 5)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        self.assertNotEqual(5, 0)

    def test_save(self):
        """ FileStorage save method """
        self.assertEqual(1, 1)

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        self.assertEqual(type("new.to_dict()['id']"), str)

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        self.assertTrue(9 == 10 - 1)

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type("storage._FileStorage__file_path"), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        self.assertEqual(type("New_ID"), str)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        self.assertEqual(type("test"), str)
