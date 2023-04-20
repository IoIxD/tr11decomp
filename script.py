import ghidrecomp

parser = ghidrecomp.get_parser()
args = parser.parse_args()
ghidrecomp.decompile(args)
