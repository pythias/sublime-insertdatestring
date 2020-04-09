# -*- encoding: UTF-8 -*-
import sublime
import sublime_plugin
import time

class InsertDateStringCommand(sublime_plugin.TextCommand):
    def run(self, edit, target='datetime'):
        self.settings = sublime.load_settings('InsertDateString.sublime-settings')
        self.edit = edit

        if target == 'datetime':
            self.insert_datetime()
        elif target == 'date':
            self.insert_date()
        elif target == 'time':
            self.insert_time()
        elif target == 'timestamp':
            self.insert_timestamp()
        elif target == 'formatted':
            self.insert_formatted()

    def insert_datetime(self):
        self.insert_by_format(self.settings.get("formatDateTime"))

    def insert_date(self):
        self.insert_by_format(self.settings.get("formatDate"))

    def insert_time(self):
        self.insert_by_format(self.settings.get("formatTime"))

    def insert_timestamp(self):
        self.insert_by_format("")

    def insert_formatted(self):
        window = self.view.window()
        window.show_input_panel("Date Time format", "%Y-%m-%d %H:%M:%s", self.insert_by_format, None, None)

    def insert_by_format(self, format):
        for sel in self.view.sel():
            if sel.empty():
                self.view.insert(self.edit, sel.a, time.strftime(format))
            else:
                self.view.replace(self.edit, sel, time.strftime(format))
