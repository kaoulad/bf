import lib.evalbf as evalbf

def pos_brackets(code):
    opening = list()
    loop = dict()
    
    for i,c in enumerate(code):
        if c == '[':
            opening.append(i)
        elif c == ']':
            begin = opening.pop()
            loop[begin] = i

    return dict(sorted(loop.items()))

def parse(c, parsed):

    if c != '':
        if c[:1] == '+':
            parsed.append(evalbf.Incr())
            return parse(c[1:], parsed)

        elif c[:1] == '-':
            parsed.append(evalbf.Decr())
            return parse(c[1:], parsed)

        elif c[:1] == '>':
            parsed.append(evalbf.MoveIncr())
            return parse(c[1:], parsed)

        elif c[:1] == '<':
            parsed.append(evalbf.MoveDecr())
            return parse(c[1:], parsed)

        elif c[:1] == '.':
            parsed.append(evalbf.Output())
            return parse(c[1:], parsed)

        elif c[:1] == ',':
            parsed.append(evalbf.Input())
            return parse(c[1:], parsed)

        elif c[:1] == '[':
            br = list(pos_brackets(c).items())[0]
            content = parse(c[1:br[1]], [])
            parsed.append(evalbf.Loop(content))
            return parse(c[br[1]:], parsed)

        else:
           return parse(c[1:], parsed)

    else:
        return parsed
