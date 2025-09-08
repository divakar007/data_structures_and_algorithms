class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        curr = path.split('/')
        res_path = []

        for d in curr:
            if d == "" or d == ".":
                continue
            if d == '..' and res_path:
                res_path.pop(-1)                
            if d != '..':
                res_path.append(d)

        if not res_path:
            return '/'
        return '/' + '/'.join(res_path)

        