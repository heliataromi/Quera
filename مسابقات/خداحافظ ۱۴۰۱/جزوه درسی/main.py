n = int(input())
volumes = list(map(int, input().split()))
end_of_semester = max(volumes)
half_of_semester = 0
volumes.remove(end_of_semester)
for volume in volumes:
	if sum(volumes) - volume == end_of_semester:
		half_of_semester = volume
		break
print(f'{half_of_semester} {end_of_semester}')