import sys

redirect_template = """
    <RoutingRule>
        <Condition>
            <KeyPrefixEquals>{from}</KeyPrefixEquals>
        </Condition>
        <Redirect>
            <ReplaceKeyWith>{to}</ReplaceKeyWith>
        </Redirect>
    </RoutingRule>
"""
def rule_generator(line):
    try:
        f, t = line.split()
    except Exception:
        print "Invalid line: {0}".format(line)
    args = {"from": f, "to": t}
    return redirect_template.format(**args)

if __name__ == "__main__":
    """
    Takes a single input file with one redirect per line. Redirects should be in the format:
    from    to
    Prints out the redirects to copy into the S3 redirect page.
    """
    if len(sys.argv) < 2:
        print "Requires an input file"
        sys.exit(1)
    input_filename = sys.argv[1]
    rules = "<RoutingRules>"
    for line in open(input_filename).readlines():
        rules += rule_generator(line)
    rules += "</RoutingRules>"
    print rules
