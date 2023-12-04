1.
pip install modal-client
modal token new

2.
# リモート側で動く関数
@stub.function()
def square(x):
    print("This code is running on a remote worker!")
    return x**2

# プログラムのローカル側のエントリポイント(プログラムの中で最初に呼び出されるところ)
@stub.local_entrypoint()
def main():
    # Modalの関数は`<function_name>.remote`で呼び出す必要がある
    print("the square is", square.remote(42))
3.
modal run get_started.py
