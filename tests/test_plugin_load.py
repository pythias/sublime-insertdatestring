import time
import sublime
from unittesting import DeferrableTestCase

class TestPluginLoad(DeferrableTestCase):
    def setUp(self):
        self.view = sublime.active_window().new_file()
        self.settings = sublime.load_settings('InsertDateString.sublime-settings')

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().run_command("close_file")

    def testPluginIsLoaded(self):
        yield 1000
        self.view.window().focus_view(self.view)
        self.view.run_command('insert_date_string', 'date')
        yield 1000
        date = time.strftime(self.settings.get("formatDate"))
        self.assertIsNotNone(self.view.find(date, 0))
