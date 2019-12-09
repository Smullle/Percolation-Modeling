# Option one for logic solution

# def search_neighbours(array, pos_array):
#     print(pos_array)
#     origin = pos_array[0]
#     n = pos_array[1]
#     s = pos_array[2]
#     w = pos_array[3]
#     e = pos_array[4]
#     # 0 is falsy
#     if not (array[np.split(n, 2)] and array[np.split(s, 2)] and array[np.split(w, 2)] and array[np.split(e, 2)]):
#         # TODO add cluster count
#         assign_clusters(origin)
#
#     if array[np.split(n, 2)] and not (array[np.split(s, 2)] and array[np.split(w, 2)] and array[np.split(e, 2)]):
#         # TODO add cluster count
#         assign_clusters(origin)
#
#     elif array[np.split(n, 2)] and not (array[np.split(s, 2)] and array[np.split(w, 2)] and array[np.split(e, 2)]):
#         # TODO add custer number
#         assign_clusters(origin)
#
#     elif not array[np.split(n, 2)] and array[np.split(s, 2)] and not (array[np.split(w, 2)] and array[np.split(e, 2)]):
#         # TODO add custer number
#         assign_clusters(origin)
#
#     elif not (array[np.split(n, 2)] and array[np.split(s, 2)] and array[np.split(w, 2)]) and not array[np.split(e, 2)]:
#         # TODO add custer number
#         assign_clusters(origin)
#
#     return 0