import sys
import io
from test.support import captured_stdout

def load(fname):
    return compile(open(fname, encoding="utf-8").read(), fname, "exec")

def check(prog, in_out):
    for input, output in in_out:
        sys.stdin = io.StringIO('\n'.join(map(str, input)))
        print('Testing input', input, '...', end=' ')
        sys.stdout.flush()
        try:
            with captured_stdout() as stdout:
                exec(load(prog), {}, {})
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
