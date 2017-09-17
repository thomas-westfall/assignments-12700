def piglatinify(s):
    ans = ''
    if not s[0].lower() in ['a','e','i','o','u']:
        ans = s[1:] + s[0] + 'ay'
    else:
        ans = s + 'ay'
    return ans