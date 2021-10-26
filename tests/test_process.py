from src.process.process import kill_process
from unittest import TestCase
import os, subprocess
from src.constants import NOTEPAD_WINDOWS

class ProcessTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()


    def test_kill_process(self):
        os.system(NOTEPAD_WINDOWS)
        kill_process(NOTEPAD_WINDOWS)
        call = 'TASKLIST', '/FI', 'imagename eq %s' % NOTEPAD_WINDOWS
        
        output = subprocess.check_output(call)
        
        last_line = output.strip().split('\r\n')[-1]
        
        process_running = last_line.lower().startswith(NOTEPAD_WINDOWS).lower()
        self.assertEqual(False, process_running)
    
    
    def tearDown(self) -> None:
        return super().tearDown()