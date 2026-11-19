class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]

            for email in emails:
                email_to_name[email] = name

            first = emails[0]

            for email in emails[1:]:
                graph[first].append(email)
                graph[email].append(first)

        visited = set()
        ans = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)

        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)

                ans.append(
                    [email_to_name[email]] + sorted(component)
                )

        return ans