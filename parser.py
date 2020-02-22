import evalbf


def parse_loop(code, parsedLoop):
        in_loop = code[1:][0:code[1:].index(']')]
        out_loop = code[1:][code[1:].index(']')+1:]

        parsed_ = parse(in_loop, [])
        return {"parsed_loop": evalbf.Loop(parsed_), "out_loop": out_loop}
        

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

        else:
            parsing_loop = parse_loop(c, [])
            parsed.append( parsing_loop['parsed_loop'] )
            return parse(parsing_loop['out_loop'], parsed)

    else:
        return parsed