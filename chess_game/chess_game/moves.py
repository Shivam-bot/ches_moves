from .constants import *


def get_moves(piece_to_move: str, positions: dict):
    CHESSBOARD = [[f"{col}{row}" for col in COLS] for row in ROWS]

    reverse_position = {value: key for key, value in positions.items()}
    chess_board_replica = CHESSBOARD
    cell_name_index_dict = {}
    chess_replica = CHESSBOARD
    for row_index, row in enumerate(CHESSBOARD):
        for cell_index, cell_name in enumerate(row):
            chess_replica[row_index][cell_index] = reverse_position.get(cell_name, None)
            cell_name_index_dict[cell_name] = (row_index, cell_index)

    pre_invalid_moves = []
    pre_valid_moves = []

    if piece_to_move.upper().startswith("W"):
        my_friends = WFriend
        my_enemies = BFriend
    else:
        my_friends = BFriend
        my_enemies = WFriend


    for key, value in positions.items():
        if KING.__contains__(key):
            if key == piece_to_move:
                pre_valid_moves = get_king_moves(key, positions.get(piece_to_move), chess_board_replica,
                                                 cell_name_index_dict, my_enemies, my_friends)
            elif my_enemies.__contains__(key):
                pre_invalid_moves.extend(get_king_moves(key, positions.get(key), chess_board_replica,
                                                        cell_name_index_dict, my_friends,my_enemies))
        elif QUEEN.__contains__(key):
            if key == piece_to_move:

                pre_valid_moves = get_queen_moves(key, positions.get(piece_to_move), chess_board_replica,
                                                  cell_name_index_dict, my_enemies, my_friends)
            elif my_enemies.__contains__(key):
                pre_invalid_moves.extend(get_queen_moves(key, positions.get(key), chess_board_replica,
                                                         cell_name_index_dict, my_friends,my_enemies))

        elif BISHOP.__contains__(key):
            if key == piece_to_move:
                pre_valid_moves = get_bishop_moves(key, positions.get(piece_to_move), chess_board_replica,
                                                   cell_name_index_dict, my_enemies, my_friends)
            elif my_enemies.__contains__(key):
                pre_invalid_moves.extend(get_bishop_moves(key, positions.get(key), chess_board_replica,
                                                          cell_name_index_dict,my_friends,my_enemies))

        elif ROOK.__contains__(key):
            if key == piece_to_move:
                pre_valid_moves = get_rook_moves(key, positions.get(piece_to_move), chess_board_replica,
                                                 cell_name_index_dict, my_enemies, my_friends)
            elif my_enemies.__contains__(key):
                pre_invalid_moves.extend(get_rook_moves(key, positions.get(key), chess_board_replica,
                                                        cell_name_index_dict, my_friends,my_enemies))
        elif KNIGHT.__contains__(key):
            if key == piece_to_move:
                pre_valid_moves = get_knight_moves(key, positions.get(piece_to_move), chess_board_replica,
                                                   cell_name_index_dict, my_enemies, my_friends)
            elif my_enemies.__contains__(key):
                pre_invalid_moves.extend(get_knight_moves(key, positions.get(key), chess_board_replica,
                                                          cell_name_index_dict,my_friends,my_enemies))

        elif PAWN.__contains__(key):
            if key == piece_to_move:
                pre_valid_moves = get_pawns_move(key, positions.get(piece_to_move), chess_board_replica,
                                                 cell_name_index_dict, my_enemies, my_friends)
            elif my_enemies.__contains__(key):
                pre_invalid_moves.extend(get_pawns_move(key, positions.get(key), chess_board_replica,
                                                      cell_name_index_dict,my_friends,my_enemies))

    return get_valid_list(pre_valid_moves, pre_invalid_moves)


def get_king_moves(king_name: str, current_position: str, positions_array: list, cell_name_index_dict: dict, my_enemies,
                   my_friends):
    valid_moves = get_forward_backward_move(current_position, positions_array, cell_name_index_dict, 1, my_enemies, 1,
                                            True)
    valid_moves.extend(get_side_moves(current_position, positions_array, cell_name_index_dict, 1, my_enemies))
    valid_moves.extend(get_diagonal_moves(current_position, positions_array, cell_name_index_dict, 1, my_enemies, True))

    return valid_moves


def get_queen_moves(queen_name: str, current_position: str, positions_array: list, cell_name_index_dict: dict,
                    my_enemies, my_friends):
    valid_moves = []
    valid_moves = get_forward_backward_move(current_position, positions_array, cell_name_index_dict, 8, my_enemies, 1,
                                            True)
    valid_moves.extend(get_side_moves(current_position, positions_array, cell_name_index_dict, 8, my_enemies))
    valid_moves.extend(get_diagonal_moves(current_position, positions_array, cell_name_index_dict, 8, my_enemies, True))

    return valid_moves


def get_bishop_moves(bishop_name: str, current_position: str, positions_array: list, cell_name_index_dict: dict,
                     my_enemies, my_friends):
    valid_moves = get_diagonal_moves(current_position, positions_array, cell_name_index_dict, 8, my_enemies, True)

    return valid_moves


def get_rook_moves(bishop_name: str, current_position: str, positions_array: list, cell_name_index_dict: dict,
                   my_enemies, my_friends):
    valid_moves = get_forward_backward_move(current_position, positions_array, cell_name_index_dict, 8, my_enemies, 1,
                                            True)
    valid_moves.extend(get_side_moves(current_position, positions_array, cell_name_index_dict, 8, my_enemies))

    return valid_moves


def get_knight_moves(bishop_name: str, current_position: str, positions_array: list, cell_name_index_dict: dict,
                     my_enemies, my_friends):
    valid_moves = []

    pre_valid_moves = get_forward_backward_move(current_position, positions_array, cell_name_index_dict, 2, my_enemies,
                                                2, True, True,True)
    for pos in pre_valid_moves:
        moves = get_side_moves(pos, positions_array, cell_name_index_dict, 1, my_enemies)
        valid_moves.extend(moves)

    pre_valid_moves = get_side_moves(current_position, positions_array, cell_name_index_dict, 2, my_enemies, True, 2)
    for pos in pre_valid_moves:
        moves = get_forward_backward_move(pos, positions_array, cell_name_index_dict, 1, my_enemies, 1,
                                          True, True)
        valid_moves.extend(moves)

    return valid_moves


def get_pawns_move(pawn_name: str, current_position: str, positions_array: list, cell_name_index_dict: dict, my_enemies,
                   my_friends):
    valid_moves = get_forward_backward_move(current_position, positions_array, cell_name_index_dict, 1, my_enemies,
                                            1, False, False, False)
    valid_moves.extend(
        get_diagonal_moves(current_position, positions_array, cell_name_index_dict, 1, my_enemies, False, False))
    return valid_moves


def get_forward_backward_move(current_position: str, positions_array: list, cell_name_index_dict: dict, steps: int,
                              enemy_list: list, step_at_once: int = 1, backward_allowed: bool = False,
                              cross_friend: bool = False, kill_enemy: bool = True):

    row, col = cell_name_index_dict.get(current_position, (None, None))


    valid_moves = []
    if col is not None and row is not None:
        max_step_forward = 8 if row + steps + 1 > 7 else row + steps + 1
        for i in range(row + 1, max_step_forward):
            # if i <= 7:
            col_name = f'{COLS[col]}{ROWS[i]}'
            current_piece_cell = positions_array[i][col]
            x = i
            if row % 2 != 0:
                x += 1

            if x % step_at_once == 0:
                if current_piece_cell is None:
                    valid_moves.append(col_name)
                elif enemy_list.__contains__(current_piece_cell) and kill_enemy:
                    valid_moves.append(col_name)
                    break
                else:
                    if cross_friend:
                        valid_moves.append(col_name)
                    break

        if backward_allowed:
            min_step_backward = -1 if row - steps - 1 < 0 else row - steps - 1
            for i in range(row - 1, min_step_backward, -1):
                col_name = f'{COLS[col]}{ROWS[i]}'
                current_piece_cell = positions_array[i][col]
                x = i
                if row % 2 != 0:
                    x += 1
                if x % step_at_once == 0:

                    if current_piece_cell is None:
                        valid_moves.append(col_name)
                    elif (current_piece_cell in enemy_list and kill_enemy) or cross_friend:
                        valid_moves.append(col_name)
                        break
                    else:
                        break

    return valid_moves


def get_side_moves(current_position: str, positions_array: list, cell_name_index_dict: dict, steps: int,
                   enemy_list: list, cross_friend: bool = False, steps_at_once: int = 1):
    row, col = cell_name_index_dict.get(current_position, (None, None))
    valid_moves = []

    if row is not None and col is not None:

        right_most_path = 8 if col + steps+1 > 7 else col + steps +1

        for i in range(col + 1, right_most_path):
            x = i
            if col % 2 != 0:
                x += 1

            if x % steps_at_once == 0:

                col_name = f'{COLS[i]}{ROWS[row]}'
                current_piece_cell = positions_array[row][i]
                if current_piece_cell is None:
                    valid_moves.append(col_name)
                elif current_piece_cell in enemy_list:
                    valid_moves.append(col_name)
                    break
                else:
                    if cross_friend:
                        valid_moves.append(col_name)
                    break

        left_most_path = -1 if col - steps -1 < 0 else col - steps -1

        for i in range(col - 1, left_most_path, -1):

            x = i
            if col % 2 != 0:
                x += 1

            if x % steps_at_once == 0:


                col_name = f'{COLS[i]}{ROWS[row]}'
                current_piece_cell = positions_array[row][i]
                if current_piece_cell is None:
                    valid_moves.append(col_name)
                elif current_piece_cell in enemy_list:
                    valid_moves.append(col_name)
                    break
                else:
                    if cross_friend:
                        valid_moves.append(col_name)
                    break

    return valid_moves


def get_diagonal_moves(current_position: str, positions_array: list, cell_name_index_dict: dict, steps: int,
                       enemy_list: list, backward_allowed: bool = False, free_move: bool = True):
    row, col = cell_name_index_dict.get(current_position, (None, None))
    valid_moves = []

    if col is not None and row is not None:
        break_right = False
        break_left = False
        upper_most_path = 8 if row + 1 + steps > 7 else row + 1 + steps

        for i in range(row + 1, upper_most_path):
            col_diff = i - row
            if not break_right and 0 <= col - col_diff < 8:
                current_piece_cell_forward_left_name = f'{COLS[col - col_diff]}{ROWS[i]}'
                current_piece_cell_forward_left = positions_array[i][col - col_diff]
                if current_piece_cell_forward_left is None and free_move:
                    valid_moves.append(current_piece_cell_forward_left_name)
                elif enemy_list.__contains__(current_piece_cell_forward_left):
                    valid_moves.append(current_piece_cell_forward_left_name)
                    break_right = True
                else:
                    break_right = True

            if not break_left and 0 <= col + col_diff < 8 :
                current_piece_cell_forward_right_name = f'{COLS[col + col_diff]}{ROWS[i]}'
                current_piece_cell_forward_right = positions_array[i][col + col_diff]

                if current_piece_cell_forward_right is None and free_move:
                    valid_moves.append(current_piece_cell_forward_right_name)
                elif enemy_list.__contains__(current_piece_cell_forward_right):
                    valid_moves.append(current_piece_cell_forward_right_name)
                    break_left = True
                else:
                    break_left = True

            if break_left and break_right:
                break

        break_right = False
        break_left = False

        if backward_allowed:

            lower_most_path = -1 if row - steps - 1 < 0 else row - steps - 1
            for i in range(row - 1, lower_most_path, -1):
                col_diff = row - i
                if not break_right and  0 <= col + col_diff < 8:
                    current_piece_cell_backward_right_name = f'{COLS[col + col_diff]}{ROWS[i]}'
                    current_piece_cell_backward_right = positions_array[i][col + col_diff]
                    if current_piece_cell_backward_right is None and free_move:
                        valid_moves.append(current_piece_cell_backward_right_name)
                    elif enemy_list.__contains__(current_piece_cell_backward_right):
                        valid_moves.append(current_piece_cell_backward_right_name)
                        break_right = True
                    else:
                        break_right = True

                if not break_left and 0 <= col - col_diff < 8:
                    current_piece_cell_backward_left_name = f'{COLS[col - col_diff]}{ROWS[i]}'
                    current_piece_cell_backward_left = positions_array[i][col - col_diff]

                    if current_piece_cell_backward_left is None and free_move:
                        valid_moves.append(current_piece_cell_backward_left_name)
                    elif enemy_list.__contains__(current_piece_cell_backward_left):
                        valid_moves.append(current_piece_cell_backward_left_name)
                        break_left = True
                    else:
                        break_left = True

                if break_left and break_right:
                    break

        return valid_moves


def get_valid_list(pre_valid_list: list, pre_invalid_list: list):
    pre_valid_list = list(set(pre_valid_list))
    pre_invalid_list = list(set(pre_invalid_list))

    valid_list_small = len(pre_valid_list) <= len(pre_invalid_list)

    invalid_list = []
    if valid_list_small:

        for pos in pre_valid_list:
            if pre_invalid_list.__contains__(pos):
                invalid_list.append(pos)
    else:

        for pos in pre_invalid_list:
            if pre_valid_list.__contains__(pos):
                invalid_list.append(pos)

    for pos in invalid_list:
        pre_valid_list.remove(pos)
    return pre_valid_list
