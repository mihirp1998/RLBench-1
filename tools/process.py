import os
import ipdb
folder_name = '/home/mprabhud/RLBench/rlbench/tasks'
dataset_name = '/mnt/ssd/mprabhud/rlbench_demos/'
st = ipdb.set_trace

current_tasks = os.listdir(dataset_name)

# ['take_toilet_roll_off_stand', 'take_lid_off_saucepan', 'put_all_groceries_in_cupboard', 'meat_off_grill', 'push_buttons', 'put_rubbish_in_color_bin', 'move_hanger', 'hit_ball_with_queue', 'open_window', 'hockey', 'put_item_in_drawer', 'setup_chess', 'put_knife_in_knife_block', 'put_plate_in_colored_dish_rack', 'put_toilet_roll_on_stand', 'scoop_with_spatula', 'put_umbrella_in_umbrella_stand', 'empty_container', 'put_knife_on_chopping_board', 'tv_on', 'close_fridge', 'put_groceries_in_cupboard', 'slide_cabinet_open_and_place_cups', 'place_wine_at_rack_location', 'toilet_seat_down', 'reach_and_drag', 'meat_on_grill', 'take_frame_off_hanger', 'slide_block_to_target', 'place_cups', 'close_grill', 'straighten_rope', 'close_microwave', 'open_wine_bottle', 'pick_and_lift', 'open_door', 'lamp_off', 'take_plate_off_colored_dish_rack', 'put_tray_in_oven', 'open_microwave', 'slide_cabinet_open', 'close_door', 'open_oven', 'set_clock_to_time', 'light_bulb_out', 'set_the_table', 'pick_up_cup', 'put_books_on_bookshelf', 'turn_tap', 'take_tray_out_of_oven', 'take_usb_out_of_computer', 'close_laptop_lid', 'hang_frame_on_hanger', 'close_jar', 'wipe_desk', 'close_drawer', 'turn_oven_on', 'remove_cups', 'pour_from_cup_to_cup', 'insert_usb_in_computer', 'change_channel', 'open_fridge', 'take_off_weighing_scales', 'open_grill', 'stack_wine', 'press_switch', 'get_ice_from_fridge', 'take_money_out_safe', 'play_jenga', 'put_books_at_shelf_location', 'solve_puzzle', 'open_jar', 'lamp_on', 'open_drawer', 'plug_charger_in_power_supply', 'stack_blocks', 'change_clock', 'weighing_scales', 'put_rubbish_in_bin', 'phone_on_base', 'beat_the_buzz', 'push_button', 'put_shoes_in_box', 'put_bottle_in_fridge', 'setup_checkers', 'reach_target', 'screw_nail', 'stack_cups', 'toilet_seat_up', 'place_hanger_on_rack', 'water_plants', 'sweep_to_dustpan_of_size', 'basketball_in_hoop', 'insert_onto_square_peg', 'block_pyramid', 'slide_block_to_color_target', 'take_umbrella_out_of_umbrella_stand', 'take_item_out_of_drawer', 'put_money_in_safe', 'unplug_charger', 'take_cup_out_from_cabinet', 'empty_dishwasher', 'place_shape_in_shape_sorter', 'open_box', 'close_box', 'sweep_to_dustpan', 'light_bulb_in', 'take_shoes_out_of_box']

all_tasks = ['take_toilet_roll_off_stand','take_lid_off_saucepan','put_all_groceries_in_cupboard','meat_off_grill',
'push_buttons','put_rubbish_in_color_bin','move_hanger','hit_ball_with_queue',
'open_window','hockey','put_item_in_drawer','setup_chess',
'put_knife_in_knife_block','put_plate_in_colored_dish_rack','put_toilet_roll_on_stand','scoop_with_spatula',
'put_umbrella_in_umbrella_stand','empty_container','put_knife_on_chopping_board','tv_on',
'close_fridge','put_groceries_in_cupboard','slide_cabinet_open_and_place_cups','place_wine_at_rack_location',
'toilet_seat_down','reach_and_drag','meat_on_grill','take_frame_off_hanger',
'slide_block_to_target','place_cups','close_grill','straighten_rope',
'close_microwave','open_wine_bottle','pick_and_lift','open_door',
'lamp_off','take_plate_off_colored_dish_rack','put_tray_in_oven','open_microwave',
'slide_cabinet_open','close_door','open_oven','set_clock_to_time',
'light_bulb_out','set_the_table','pick_up_cup','put_books_on_bookshelf',
'turn_tap','take_tray_out_of_oven','take_usb_out_of_computer','close_laptop_lid',
'hang_frame_on_hanger','close_jar','wipe_desk','close_drawer',
'turn_oven_on','remove_cups','pour_from_cup_to_cup','insert_usb_in_computer',
'change_channel','open_fridge','take_off_weighing_scales','open_grill',
'stack_wine','press_switch','get_ice_from_fridge','take_money_out_safe',
'play_jenga','put_books_at_shelf_location','solve_puzzle','open_jar',
'lamp_on','open_drawer','plug_charger_in_power_supply','stack_blocks',
'change_clock','weighing_scales','put_rubbish_in_bin','phone_on_base',
'beat_the_buzz','push_button','put_shoes_in_box','put_bottle_in_fridge',
'setup_checkers','reach_target','screw_nail','stack_cups',
'toilet_seat_up','place_hanger_on_rack','water_plants','sweep_to_dustpan_of_size',
'basketball_in_hoop','insert_onto_square_peg','block_pyramid','slide_block_to_color_target',
'take_umbrella_out_of_umbrella_stand','take_item_out_of_drawer','put_money_in_safe','unplug_charger',
'take_cup_out_from_cabinet','empty_dishwasher','place_shape_in_shape_sorter','open_box',
'close_box','sweep_to_dustpan','light_bulb_in','take_shoes_out_of_box']
print(len(all_tasks))
print([i for i in current_tasks if i in all_tasks])
[all_tasks.remove(i) for i in current_tasks if i in all_tasks]
print(all_tasks)
print(len(all_tasks))
