import torch

x = torch.empty(5, 3)
print(x)

x = torch.rand(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)

x = x.new_ones(5, 3, dtype=torch.double)

# new_* methods take in sizes
print(x)

x = torch.randn_like(x, dtype=torch.float)

# override dtype!
print(x)

# result has the same size

print(x.size())

y = torch.ones(5, 3)
print(x + y)

print(torch.add(x, y))

print(x[:, 1])

x = torch.randn(8, 4)
y = x.view(32)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

x = torch.rand(1)
print(x)
print(x.item())