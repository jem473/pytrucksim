from memory_map import BinaryMemoryMap
from config import *

class Telemetry:
    class Trailer:
        def __init__(self, sdk):
            self.wheel_steerable = sdk.mm.read('bool16')
            self.wheel_simulated = sdk.mm.read('bool16')
            self.wheel_powered = sdk.mm.read('bool16')
            self.wheel_liftable = sdk.mm.read('bool16')

            self.wheel_on_ground = sdk.mm.read('bool16')
            self.attached = sdk.mm.read('bool')

            sdk.mm.advance(3)

            self.wheel_substance = sdk.mm.read('uint16')

            self.wheel_count = sdk.mm.read('uint')

            self.cargo_damage = sdk.mm.read('float')
            self.wear_chassis = sdk.mm.read('float')
            self.wear_wheels = sdk.mm.read('float')
            self.wheel_susp_deflection = sdk.mm.read('float16')
            self.wheel_velocity = sdk.mm.read('float16')
            self.wheel_steering = sdk.mm.read('float16')
            self.wheel_rotation = sdk.mm.read('float16')
            self.wheel_lift = sdk.mm.read('float16')
            self.wheel_lift_offset = sdk.mm.read('float16')

            self.wheel_radius = sdk.mm.read('float16')

            self.linear_velocity_x = sdk.mm.read('float')
            self.linear_velocity_y = sdk.mm.read('float')
            self.linear_velocity_z = sdk.mm.read('float')
            self.angular_velocity_x = sdk.mm.read('float')
            self.angular_velocity_y = sdk.mm.read('float')
            self.angular_velocity_z = sdk.mm.read('float')
            self.linear_acceleration_x = sdk.mm.read('float')
            self.linear_acceleration_y = sdk.mm.read('float')
            self.linear_acceleration_z = sdk.mm.read('float')
            self.angular_acceleration_x = sdk.mm.read('float')
            self.angular_acceleration_y = sdk.mm.read('float')
            self.angular_acceleration_z = sdk.mm.read('float')

            self.hook_position_x = sdk.mm.read('float')
            self.hook_position_y = sdk.mm.read('float')
            self.hook_position_z = sdk.mm.read('float')
            self.wheel_position_x = sdk.mm.read('float16')
            self.wheel_position_y = sdk.mm.read('float16')
            self.wheel_position_z = sdk.mm.read('float16')

            self.world_x = sdk.mm.read('double')
            self.world_y = sdk.mm.read('double')
            self.world_z = sdk.mm.read('double')
            self.rotation_x = sdk.mm.read('double')
            self.rotation_y = sdk.mm.read('double')
            self.rotation_z = sdk.mm.read('double')

            self.id = sdk.mm.read('string')
            self.cargo_accessory_id = sdk.mm.read('string')
            self.body_type = sdk.mm.read('string')
            self.brand_id = sdk.mm.read('string')
            self.brand = sdk.mm.read('string')
            self.name = sdk.mm.read('string')
            self.chain_type = sdk.mm.read('string')
            self.license_plate = sdk.mm.read('string')
            self.license_plate_country = sdk.mm.read('string')
            self.license_plate_country_id = sdk.mm.read('string')

    def __init__(self):
        self.mm = BinaryMemoryMap(HANDLE, MM_NAME, MM_SIZE, MM_TYPES)
        self.update()
    
    def speed_mph(self):
        return self.speed * 2.237
    
    def speed_kph(self):
        return self.speed * 3.6

    def update(self):
        self.mm.update()
        self.data = {}
        self.sdk_active = self.mm.read('bool')
        self.mm.advance(3)
        self.paused = self.mm.read('bool')
        self.mm.advance(3)

        self.time = self.mm.read('unsigned long long')
        self.simulated_time = self.mm.read('unsigned long long')
        self.render_time = self.mm.read('unsigned long long')
        
        self.mm.advance(8)

        # Offset 40
        #assert self.mm.current_offset() == 40

        self.telemetry_plugin_revision = self.mm.read('uint')
        self.version_major = self.mm.read('uint')
        self.version_minor = self.mm.read('uint')
        self.game = self.mm.read('uint')
        self.game_text = 'ets2' if self.game == 1 else 'ats'
        self.telemetry_version_game_major = self.mm.read('uint')
        self.telemetry_version_game_minor = self.mm.read('uint')

        self.time_abs = self.mm.read('uint')
        self.gears = self.mm.read('uint')
        self.gears_reverse = self.mm.read('uint')
        self.retarder_step_count = self.mm.read('uint')
        self.truck_wheel_count = self.mm.read('uint')
        self.selector_count = self.mm.read('uint')
        self.time_abs_delivery = self.mm.read('uint')
        self.max_trailer_count = self.mm.read('uint')
        self.unit_count = self.mm.read('uint')
        self.planned_distance_km = self.mm.read('uint')

        self.shifter_slot = self.mm.read('uint')
        self.retarder_brake = self.mm.read('uint')
        self.lights_front_aux = self.mm.read('uint')
        self.lights_front_roof = self.mm.read('uint')
        self.truck_wheelsubstance = self.mm.read('uint16')
        self.hshifter_position = self.mm.read('uint32')
        self.hshifter_bitmask = self.mm.read('uint32')

        self.job_delivered_delivery_time = self.mm.read('uint')
        self.job_starting_time = self.mm.read('uint')
        self.job_finished_time = self.mm.read('uint')

        self.mm.advance(48)

        self.rest_stop = self.mm.read('int')
        self.gear = self.mm.read('int')
        self.gear_dashboard = self.mm.read('int')
        self.hshifter_resulting = self.mm.read('int32')

        self.job_delivered_earned_xp = self.mm.read('int')

        self.mm.advance(56)

        self.scale = self.mm.read('float')

        self.fuel_capacity = self.mm.read('float')
        self.fuel_warning_factor = self.mm.read('float')
        self.adblue_capacity = self.mm.read('float')
        self.adblue_warning_factor = self.mm.read('float')
        self.air_pressure_warning = self.mm.read('float')
        self.air_pressure_emergency = self.mm.read('float')
        self.oil_pressure_warning = self.mm.read('float')
        self.water_temperature_warning = self.mm.read('float')
        self.battery_voltage_warning = self.mm.read('float')
        self.engine_rpm_max = self.mm.read('float')
        self.gear_differential = self.mm.read('float')
        self.cargo_mass = self.mm.read('float')
        self.truck_wheel_radius = self.mm.read('float16')
        self.gear_ratios_forward = self.mm.read('float24')
        self.gear_ratios_reverse = self.mm.read('float8')
        self.unit_mass = self.mm.read('float')

        self.speed = self.mm.read('float') # In m/s
        self.engine_rpm = self.mm.read('float')
        self.user_steer = self.mm.read('float')
        self.user_throttle = self.mm.read('float')
        self.user_brake = self.mm.read('float')
        self.user_clutch = self.mm.read('float')
        self.game_steer = self.mm.read('float')
        self.game_throttle = self.mm.read('float')
        self.game_brake = self.mm.read('float')
        self.game_clutch = self.mm.read('float')
        self.cruise_control_speed = self.mm.read('float')
        self.air_pressure = self.mm.read('float')
        self.brake_temperature = self.mm.read('float')
        self.fuel = self.mm.read('float')
        self.fuel_avg_consumption = self.mm.read('float')
        self.fuel_range = self.mm.read('float')
        self.adblue = self.mm.read('float')
        self.oil_pressure = self.mm.read('float')
        self.oil_temperature = self.mm.read('float')
        self.water_temperature = self.mm.read('float')
        self.battery_voltage = self.mm.read('float')
        self.lights_dashboard = self.mm.read('float')
        self.wear_engine = self.mm.read('float')
        self.wear_transmission = self.mm.read('float')
        self.wear_cabin = self.mm.read('float')
        self.wear_chassis = self.mm.read('float')
        self.wear_wheels = self.mm.read('float')
        self.truck_odometer = self.mm.read('float')
        self.route_distance = self.mm.read('float')
        self.route_time = self.mm.read('float')
        self.speed_limit = self.mm.read('float')
        self.truck_wheel_susp_deflection = self.mm.read('float16')
        self.truck_wheel_velocity = self.mm.read('float16')
        self.truck_wheel_steering = self.mm.read('float16')
        self.truck_wheel_rotation = self.mm.read('float16')
        self.truck_wheel_lift = self.mm.read('float16')
        self.truck_wheel_lift_offset = self.mm.read('float16')

        self.job_delivered_cargo_damage = self.mm.read('float')
        self.job_delivered_distance_km = self.mm.read('float')
        self.refuel_amount = self.mm.read('float')
        self.cargo_damage = self.mm.read('float')

        self.mm.advance(28)

        # Offset 1500
        #assert self.mm.current_offset() == 1500

        self.truck_wheel_steerable = self.mm.read('bool16')
        self.truck_wheel_simulated = self.mm.read('bool16')
        self.truck_wheel_powered = self.mm.read('bool16')
        self.truck_wheel_liftable = self.mm.read('bool16')
        self.is_cargo_loaded = self.mm.read('bool')
        self.special_job = self.mm.read('bool')

        self.park_brake = self.mm.read('bool')
        self.motor_brake = self.mm.read('bool')
        self.air_pressure_warning = self.mm.read('bool')
        self.air_pressure_emergency = self.mm.read('bool')
        self.fuel_warning = self.mm.read('bool')
        self.adblue_warning = self.mm.read('bool')
        self.oil_pressure_warning = self.mm.read('bool')
        self.water_temperature_warning = self.mm.read('bool')
        self.battery_voltage_warning = self.mm.read('bool')
        self.electric_enabled = self.mm.read('bool')
        self.engine_enabled = self.mm.read('bool')
        self.wipers = self.mm.read('bool')
        self.blinker_left_active = self.mm.read('bool')
        self.blinker_right_active = self.mm.read('bool')
        self.blinker_left_on = self.mm.read('bool')
        self.blinker_right_on = self.mm.read('bool')
        self.lights_parking = self.mm.read('bool')
        self.lights_beam_low = self.mm.read('bool')
        self.lights_beam_high = self.mm.read('bool')
        self.lights_beacon = self.mm.read('bool')
        self.lights_brake = self.mm.read('bool')
        self.lights_reverse = self.mm.read('bool')
        self.lights_hazard = self.mm.read('bool')
        self.cruise_control = self.mm.read('bool')
        self.truck_wheel_on_ground = self.mm.read('bool16')
        self.shifter_toggle = self.mm.read('bool2')
        self.differential_lock = self.mm.read('bool')
        self.lift_axle = self.mm.read('bool')
        self.lift_axle_indicator = self.mm.read('bool')
        self.trailer_lift_axle = self.mm.read('bool')
        self.trailer_lift_axle_indicator = self.mm.read('bool')

        self.job_delivered_autopark_used = self.mm.read('bool')
        self.job_delivered_autoload_used = self.mm.read('bool')

        self.mm.advance(25)

        # Offset 1640
        #assert self.mm.current_offset() == 1640

        self.cabin_position_x = self.mm.read('float')
        self.cabin_position_y = self.mm.read('float')
        self.cabin_position_z = self.mm.read('float')
        self.head_position_x = self.mm.read('float')
        self.head_position_y = self.mm.read('float')
        self.head_position_z = self.mm.read('float')
        self.truck_hook_position_x = self.mm.read('float')
        self.truck_hook_position_y = self.mm.read('float')
        self.truck_hook_position_z = self.mm.read('float')
        self.truck_wheel_position_x = self.mm.read('float16')
        self.truck_wheel_position_y = self.mm.read('float16')
        self.truck_wheel_position_z = self.mm.read('float16')
        
        self.lv_acceleration_x = self.mm.read('float')
        self.lv_acceleration_y = self.mm.read('float')
        self.lv_acceleration_z = self.mm.read('float')
        self.av_acceleration_x = self.mm.read('float')
        self.av_acceleration_y = self.mm.read('float')
        self.av_acceleration_z = self.mm.read('float')
        self.acceleration_x = self.mm.read('float')
        self.acceleration_y = self.mm.read('float')
        self.acceleration_z = self.mm.read('float')
        self.aa_acceleration_x = self.mm.read('float')
        self.aa_acceleration_y = self.mm.read('float')
        self.aa_acceleration_z = self.mm.read('float')
        self.cabin_av_x = self.mm.read('float')
        self.cabin_av_y = self.mm.read('float')
        self.cabin_av_z = self.mm.read('float')
        self.cabin_aa_x = self.mm.read('float')
        self.cabin_aa_y = self.mm.read('float')
        self.cabin_aa_z = self.mm.read('float')

        self.mm.advance(60)

        # Offset 2000
        #assert self.mm.current_offset() == 2000

        self.cabin_offset_x = self.mm.read('float')
        self.cabin_offset_y = self.mm.read('float')
        self.cabin_offset_z = self.mm.read('float')
        self.cabin_offset_rotation_x = self.mm.read('float')
        self.cabin_offset_rotation_y = self.mm.read('float')
        self.cabin_offset_rotation_z = self.mm.read('float')
        self.head_offset_x = self.mm.read('float')
        self.head_offset_y = self.mm.read('float')
        self.head_offset_z = self.mm.read('float')
        self.head_offset_rotation_x = self.mm.read('float')
        self.head_offset_rotation_y = self.mm.read('float')
        self.head_offset_rotation_z = self.mm.read('float')

        self.mm.advance(152)

        # Offset 2200
        #assert self.mm.current_offset() == 2200

        self.coordinate_x = self.mm.read('double')
        self.coordinate_y = self.mm.read('double')
        self.coordinate_z = self.mm.read('double')
        self.rotation_x = self.mm.read('double')
        self.rotation_y = self.mm.read('double')
        self.rotation_z = self.mm.read('double')
        
        self.mm.advance(52)

        # Offset 2300
       # assert self.mm.current_offset() == 2300

        self.truck_brand_id = self.mm.read('string')
        self.truck_brand = self.mm.read('string')
        self.truck_id = self.mm.read('string')

        self.truck_name = self.mm.read('string')
        self.cargo_id = self.mm.read('string')
        self.cargo = self.mm.read('string')
        self.city_dst_id = self.mm.read('string')
        self.city_dst = self.mm.read('string')
        self.comp_dst_id = self.mm.read('string')
        self.comp_dst = self.mm.read('string')
        self.city_src_id = self.mm.read('string')
        self.city_src = self.mm.read('string')
        self.comp_src_id = self.mm.read('string')
        self.comp_src = self.mm.read('string')
        self.shifter_type = self.mm.read('string16')
        
        self.truck_license_plate = self.mm.read('string')
        self.truck_license_plate_country_id = self.mm.read('string')
        self.truck_license_plate_country = self.mm.read('string')

        self.job_market = self.mm.read('string32')

        self.fine_offence = self.mm.read('string32')
        self.ferry_source_name = self.mm.read('string')
        self.ferry_target_name = self.mm.read('string')
        self.ferry_source_id = self.mm.read('string')
        self.ferry_target_id = self.mm.read('string')
        self.train_source_name = self.mm.read('string')
        self.train_target_name = self.mm.read('string')
        self.train_source_id = self.mm.read('string')
        self.train_target_id = self.mm.read('string')

        self.mm.advance(20)

        # Offset 4000
        #assert self.mm.current_offset() == 4000

        self.job_income = self.mm.read('unsigned long long')

        self.mm.advance(192)

        # Offset 4200
        assert self.mm.current_offset() == 4200

        self.job_cancelled_penalty = self.mm.read('long long')
        self.job_delivered_revenue = self.mm.read('long long')
        self.fine_amount = self.mm.read('long long')
        self.tollgate_pay_amount = self.mm.read('long long')
        self.ferry_pay_amount = self.mm.read('long long')
        self.train_pay_amount = self.mm.read('long long')

        self.mm.advance(52)

        # Offset 4300
        #assert self.mm.current_offset() == 4300

        self.on_job = self.mm.read('bool')
        self.job_finished = self.mm.read('bool')
        self.job_cancelled = self.mm.read('bool')
        self.job_delivered = self.mm.read('bool')
        self.fined = self.mm.read('bool')
        self.tollgate = self.mm.read('bool')
        self.ferry = self.mm.read('bool')
        self.train = self.mm.read('bool')
        self.refuel = self.mm.read('bool')
        self.refuel_paid = self.mm.read('bool') # This is refuel_payed in the sdk

        self.mm.advance(90)

        # Offset 4400
        #assert self.mm.current_offset() == 4400

        self.substances = []
        for _ in range(0, SUBSTANCE_SIZE):
            self.substances.append(self.mm.read('string'))
        
        # Offset 6000
        #assert self.mm.current_offset() == 6000

        self.trailers = []

        for _ in range(10):
            self.trailers.append(self.Trailer(self))

        # Offset 21520
        #assert self.mm.current_offset() == 21520
