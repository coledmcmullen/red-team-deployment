#!/usr/bin/python

from cmd import Cmd
import sys

class VCTool(Cmd):
    prompt = 'vctool > '
    intro = "[ VCENTER-TOOL ]\nType help for options.\nType exit or q to quit."

    def do_help(self, inp):
        print("1) add host [name] [OS] [RAM] [processors] [cores] \n2) add vuln [host] [vuln]  \n3) generate script \n4) load script [script] \n5) list hosts \n6) list vuln [host]")

    def do_add(self, inp):
        options = inp.split()
        if len(options) > 0:
            # vuln or host
            if options[0] == 'host':
                if len(options) >= 5:
                    # Not sure what provisioning will actually be relevant
                    name, os, ram, procs, cores = options[1:6]
                    # [Insert relevant actions with this information]
                else:
                    print("OS List:")
                    # Relevant list
            if options[0] == 'vuln':
                if len(options) > 2:
                    host, vuln = options[1:3]
                    # [Insert relevant actions with this information]
                else:
                    print("List of vulnerabilities:")
                    # Relevant list                
        else:
            print("usage: \'add host\' to see OS list\nadd host [name] [OS] [RAM] [processors] [cores]\nadd vuln [host] [vuln]")

    def do_generate(self, inp):
        if inp == 'script':
            print("Generate script.")
            # [Insert relevant actions with this information]

    def do_load(self, inp):
        options = inp.split()
        if len(options) < 2:
            print("usage: load script [script]")
        else:
            script = options[1]
            print("Loading script", script)
            # [Insert relevant actions with this information]
    
    def do_list(self, inp):
        options = inp.split()
        if len(options) > 0:
            # vuln or host
            if options[0] == 'hosts':
                print("List of hosts:")
                # Relevant list
            if options[0] == 'vuln':
                if len(options) > 1:
                    host = options[1]
                    # [Insert relevant actions with this information]
                else:
                    print("list vuln [host]")              
        else:
            print("usage: list hosts\nlist vuln [host]")
    
    def do_exit(self, inp):
        print("Bye.")
        return True

    def default(self, inp):
        if inp == 'q':
            return self.do_exit(inp)

    do_EOF = do_exit
   
if len(sys.argv) > 1:
    VCTool().onecmd(' '.join(sys.argv[1:]))
else:
    VCTool().cmdloop()