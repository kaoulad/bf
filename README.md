## bf.py

Brainfuck interpreter written in Python.

Pre-requesite:
    - python (>= 3.6)

```
python bf.py
```

In bf.py file:
```
execute(file.bf, input[optional])
```

You have to create brainfuck file.

### Examples

```
execute("hello.bf", "")

# Output: Hello World!
```

```
execute("input.bf", "hello")

# Output: hello
```

```
execute("mandelbrot.bf", "")
# Output
```

![mandelbrot](mandelbrot.png)


