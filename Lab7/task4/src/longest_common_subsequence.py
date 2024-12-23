from Lab7.utils import read_input, write_output, decorate


def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)

    # Create DP table of size (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def main():
    f = read_input(4)

    try:
        n = int(f[0].strip())
        A = list(map(int, f[1].strip().split()))
        m = int(f[2].strip())
        B = list(map(int, f[3].strip().split()))
    except ValueError as e:
        raise ValueError(f"Error parsing input: {e}")

    result = longest_common_subsequence(A, B)

    write_output(4, str(result) + "\n")


if __name__ == "__main__":
    decorate(task=4, task_name='longest_common_subsequence')