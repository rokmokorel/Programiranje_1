import sys
import io
import re
from test.support import captured_stdout

def check(prog, in_out, startswith=None):
    for input, output in in_out:
        
        src = open(prog, encoding="utf_8_sig").read().strip()
        if startswith:
            regex = r'xs\s*=\s*\[.*\]'
            if not re.match(regex, src):
                print('TEST FAILED')
                print('\nProgram se mora začeti z:\n\n{}'.format(startswith))
                return
            src = re.sub(regex, 'xs = {}'.format(input), src)
        else:
            sys.stdin = io.StringIO(input + '\n\n')

        print('Testing input', repr(input.replace("\n", " ")), '...', end=' ')
        try:
            with captured_stdout() as stdout:
                exec(src, {})
            if stdout.getvalue().rstrip() != output.rstrip():
                print('TEST FAILED')
                print('\nExpected:\n{}\nGot:\n{}'.format(output, stdout.getvalue()))
                return
        except EOFError:
            print('TEST FAILED')
            return
        print('OK')
    msg = 'TEST SUCCEEDED ({})'.format(prog)
    print('\n{emph}\n{msg}\n{emph}'.format(msg=msg, emph='=' * len(msg)))
