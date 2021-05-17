import sys
from datetime import datetime
from pathlib import Path
# from datetime import date, timedelta
import numpy as np
import netCDF4

'''
Create a sample netCDF4 UGRID file, consisting of only triangles
programmer: jan.mooiman@deltares.nl
'''

def main(ncfile):
    ncfile.createDimension("time", None)
    ncfile.createDimension("Two", 2)

    edges_2d = 59
    faces_2d = 32
    nodes_2d = 28
    ncfile.createDimension("max_nMesh2D_face_nodes", 3)
    ncfile.createDimension("nMesh2D_edge", edges_2d)
    ncfile.createDimension("nMesh2D_face", faces_2d)
    ncfile.createDimension("nMesh2D_node", nodes_2d)

    #
    # Coordinate Reference System ---------------------------------------------
    #
    crs = ncfile.createVariable("projected_coordinate_system", "u4", ())
    crs.setncattr('name', 'Unknown projected')
    crs.epsg = 28992
    crs.grid_mapping_name = 'Unknown projected'
    crs.longitude_of_prime_meridian = 0.
    crs.semi_major_axis = 6378137.
    crs.semi_minor_axis = 6356752.314245
    crs.inverse_flattening = 298.257223563
    crs.proj4_params = ""
    crs.EPSG_code = 'EPSG:28992'
    crs.projection_name = ''
    crs.wkt = ''
    crs.comment = ''
    crs.value = 'value is equal to EPSG code'

    #
    # 2D Mesh ------------------------------------------------------------------
    #
    mesh2d = ncfile.createVariable("mesh2D", "u4", ())
    mesh2d.cf_role = 'mesh_topology'
    mesh2d.edge_coordinates = 'Mesh2D_edge_x Mesh2D_edge_y'
    mesh2d.edge_dimension = 'nMesh2D_edge'
    mesh2d.edge_face_connectivity = 'Mesh2D_edge_faces'
    mesh2d.edge_node_connectivity = 'Mesh2D_edge_nodes'
    mesh2d.face_coordinates = 'Mesh2D_face_x Mesh2D_face_y'
    mesh2d.face_dimension = 'nMesh2D_face'
    mesh2d.face_edge_connectivity = 'Mesh2D_face_edges'
    mesh2d.face_face_connectivity = 'Mesh2D_face_face'
    mesh2d.face_node_connectivity = 'Mesh2D_face_nodes'
    mesh2d.long_name = "Mesh 2D"
    mesh2d.max_face_nodes_dimension = 'max_nMeshFaceNodes'
    mesh2d.node_coordinates = 'Mesh2D_node_x Mesh2D_node_y'
    mesh2d.node_dimension = 'nMesh2D_node'
    mesh2d.topology_dimension = 2

    mesh2d_x = ncfile.createVariable("Mesh2D_node_x", "f8", "nMesh2D_node")
    mesh2d_y = ncfile.createVariable("Mesh2D_node_y", "f8", "nMesh2D_node")
    mesh2d_x.standard_name = 'projection_x_coordinate'
    mesh2d_x.units = 'm'
    mesh2d_y.standard_name = 'projection_y_coordinate'
    mesh2d_y.units = 'm'
    mesh2d_x[:] = [-150, 133.043016423945, 581.589811881954, 976.640200542219,
                   1581.56110817825, 2104.17985151006, 2330.51080334667, 2820.20868095679,
                   3326.36699142775, 3836.64041011393, 4091.3328, 4091.0588, 4087.6891,
                   3547.526, 3104.2863, 2530.6819, 2009.2233, 1428.1695, 835.9416,
                   321.93246, -150, -150, 2441.32387428041, 326.036595922787,
                   3368.4335297957, 2852.91575366228, 564.605213864027, 1077.48494483683]

    mesh2d_y[:] = [625.39432, 908.781962364921, 921.127287010554,
                   464.350275122123, 155.717158981291, 443.774734046067, 600.148846224089,
                   414.968976539589, 530.1920065655, 600.148846224089, 565.79906,
                   99.9999999999999, -350, -350, -350, -350, -350, -350, -350, -350, -350,
                   99.9999999999999, 125.838619350021, 513.501770748115, 134.310966738994,
                   -5.00908866931604, 62.2847173147688, -3.38148493072237]

    mesh2d_xu = ncfile.createVariable("Mesh2D_edge_x", "f8", "nMesh2D_edge")
    mesh2d_yu = ncfile.createVariable("Mesh2D_edge_y", "f8", "nMesh2D_edge")
    mesh2d_xu.standard_name = 'projection_x_coordinate'
    mesh2d_xu.units = 'm'
    mesh2d_yu.standard_name = 'projection_y_coordinate'
    mesh2d_yu.units = 'm'
    mesh2d_xu[:] = [3963.98660505697, 3963.84960505696, 4091.1958, 
    2217.34532742836, 2272.75186289523, 2385.91733881354, 2630.7662776186, 
    2575.35974215173, 2056.70157575503, -8.4784917880275, 88.0182979613935, 
    229.539806173366, 3325.90615, 3457.97976489785, 3236.35991489785, 
    2836.56221730954, 4089.37395, 3819.2924, 3817.60755, 357.31641415295, 
    453.813203902371, -150, 85.96623, 85.96623, 2978.60102683114, 
    2691.79882683114, 2817.4841, 2486.00288714021, 3347.40026061172, 
    3073.28783619227, 3094.32110537625, 578.93703, 700.273406932013, 
    443.268836932013, 2269.9526, -150, 88.0182979613935, 207.302606932013, 
    956.713272418415, 651.338398232503, 779.115006212086, 1718.6964, 
    1795.39220408913, 1504.86530408912, 1132.05555, 1252.82722241841, 
    1329.52302650754, 1027.06257268952, 770.622707203123, 1279.10065436023, 
    1842.87047984415, 3602.53696995482, 3581.50370077084, 445.320904893407, 
    821.045079350429, 2225.27358714021, 2647.11981397135, 3110.67464172899, 
    3729.74616489785 ]

    mesh2d_yu[:] = [582.973953112044, 350.074423112044, 332.89953, 
    521.961790135078, 284.806676698044, 362.993732787055, 270.403797944805, 
    507.558911381839, 46.8873670230335, 767.088141182461, 569.448045374058, 
    711.141866556518, -350, -107.844516630503, -107.844516630503, 
    204.979943935136, -125, -125, -350, 914.954624687738, 717.314528879334, 
    -125, -350, -125, -177.504544334658, -177.504544334658, -350, 
    -112.080690324989, 332.251486652247, 472.580491552545, 274.639971639292, 
    -350, -143.857641342616, -143.857641342616, -350, 362.69716, 
    306.750885374057, 81.1423586573843, -176.690742465361, 488.926022935119, 
    692.738781066339, -350, -97.1414205093545, -97.1414205093545, -350, 
    -176.690742465361, 76.1678370252843, 230.4843950957, 263.317496218446, 
    310.033717051707, 299.745946513679, 367.229906481541, 565.170426394795, 
    287.893244031442, 29.4516161920232, -112.080690324989, 60.4147653403525, 
    64.650939034839, 117.155483369497]

    mesh2d_xmc = ncfile.createVariable("Mesh2D_face_x", "f8", "nMesh2D_face")
    mesh2d_ymc = ncfile.createVariable("Mesh2D_face_y", "f8", "nMesh2D_face")
    mesh2d_xmc.standard_name = 'projection_x_coordinate'
    mesh2d_xmc.long_name = 'x-coordinate of mesh face mass centre'
    mesh2d_xmc.units = 'm'
    mesh2d_ymc.standard_name = 'projection_y_coordinate'
    mesh2d_ymc.long_name = 'y-coordinate of mesh face mass centre'
    mesh2d_ymc.units = 'm'
    mesh2d_xmc[:] = [8.67886530759569, 103.026537448911, 346.889808076229, 
    628.088869448987, 622.427336776344, 872.910119747692, 1211.89541785243, 
    1898.3214198961, 1362.40518433836, 1672.98463605942, 2184.90900859682, 
    2292.00484304571, 2530.68111952796, 2704.81610296649, 3013.85265480492, 
    3171.66973406008, 3510.48031044579, 3765.37757996988, 4006.34400337131, 
    3669.0061099319, 3908.75796666667, 3340.08194326523, 3108.54519448599, 
    2829.29465122076, 2608.3071759809, 2327.07635809347, 1113.86534827894, 
    826.010586233619, 574.159757954676, 245.512557954676, 7.31082000000001, 
    246.880603262271]

    mesh2d_ymc[:] = [412.965363582705, 682.559351037679, 781.137006707863, 
    632.993110960264, 346.712254395002, 174.41783583539, 205.561983057564, 
    83.1639643424527, -65.8881086498105, -181.427613672903, 73.2044511320293, 
    389.920733206726, 380.3188140379, 178.599502406765, 181.423618203089, 
    359.823983281361, 421.550606509528, 278.153270987694, 421.98263540803, 
    -38.563011087002, -200, -188.563011087002, -73.5660406434407, 
    -235.003029556439, -76.390156439765, -191.387126883326, 
    -234.460494976907, -97.0322558719845, -212.571760895077, 
    -62.5717608950771, -200, 225.262162687628]
                     
    mesh2d_en = ncfile.createVariable("Mesh2D_edge_nodes", "f8", ("nMesh2D_edge", "Two"))
    mesh2d_en.cf_role = 'edge_node_connectivity'
    mesh2d_en.long_name = 'Maps every edge to the two nodes that it connects'
    mesh2d_en.start_index = 1
    mesh2d_en[:, :] = [  11, 10,
                         10, 12,
                         12, 11,
                         7, 6,
                         6, 23,
                         23, 7,
                         23, 8,
                         8, 7,
                         6, 17,
                         2, 1,
                         1, 24,
                         24, 2,
                         15, 14,
                         14, 25,
                         25, 15,
                         26, 8,
                         13, 12,
                         12, 14,
                         14, 13,
                         3, 2,
                         24, 3,
                         22, 21,
                         21, 20,
                         20, 22,
                         26, 15,
                         26, 16,
                         16, 15,
                         23, 16,
                         25, 9,
                         9, 8,
                         8, 25,
                         20, 19,
                         19, 27,
                         27, 20,
                         17, 16,
                         1, 22,
                         22, 24,
                         27, 22,
                         19, 28,
                         24, 4,
                         4, 3,
                         18, 17,
                         17, 5,
                         5, 18,
                         19, 18,
                         18, 28,
                         5, 28,
                         28, 4,
                         4, 27,
                         5, 4,
                         6, 5,
                         25, 10,
                         10, 9,
                         24, 27,
                         27, 28,
                         17, 23,
                         23, 26,
                         26, 25,
                         25, 12]

    mesh2d_fn = ncfile.createVariable("Mesh2D_face_nodes", "f8", ("nMesh2D_face", "max_nMesh2D_face_nodes"),
                                      fill_value=0)
    mesh2d_fn.cf_role = 'face_node_connectivity'
    mesh2d_fn.long_name = 'Maps every face to the nodes that it defines'
    mesh2d_fn.start_index = 1
    mesh2d_fn[:, :] = [1, 22, 24,
                       1, 24, 2,
                       2, 24, 3,
                       3, 24, 4,
                       4, 24, 27,
                       4, 27, 28,
                       4, 28, 5,
                       5, 17, 6,
                       5, 28, 18,
                       5, 18, 17,
                       6, 17, 23,
                       6, 23, 7,
                       7, 23, 8,
                       8, 23, 26,
                       8, 26, 25,
                       8, 25, 9,
                       9, 25, 10,
                       10, 25, 12,
                       10, 12, 11,
                       12, 25, 14,
                       12, 14, 13,
                       14, 25, 15,
                       15, 25, 26,
                       15, 26, 16,
                       16, 26, 23,
                       16, 23, 17,
                       18, 28, 19,
                       19, 28, 27,
                       19, 27, 20,
                       20, 27, 22,
                       20, 22, 21,
                       22, 27, 24]             
                       
    #
    # time series ------------------------------------------------------------------
    #
    times = ncfile.createVariable("time", "f8", "time")
    times.standard_name = 'time'
    times.long_name = 'Time'
    times.units = 'seconds since 2017-01-01 00:00:00'
    times.calender = 'gregorian'
    times[0] = 60.0
    times[1] = 120.0
    #
    # data on the 2D mesh ------------------------------------------------------------------
    #
    wl_2d = ncfile.createVariable("s1_2d", "f8", ("time", "nMesh2D_face"))
    wl_2d.coordinates = 'Mesh2D_face_x Mesh2D_face_y'
    wl_2d.location = 'face'
    wl_2d.long_name = 'Water level'
    wl_2d.mesh = 'mesh2D'
    wl_2d.standard_name = 'sea_surface_height_above_geoid'
    wl_2d.units = 'm'
    wl_2d[0, :] = np.linspace(2., 6., faces_2d)
    wl_2d[1, :] = np.linspace(6., 2., faces_2d)

    vel_2d = ncfile.createVariable("u_2d", "f8", ("time", "nMesh2D_edge"))
    vel_2d.coordinates = 'Mesh2D_edge_x Mesh2D_edge_y'
    vel_2d.location = 'edge'
    vel_2d.long_name = 'Normal velocity at edge'
    vel_2d.mesh = 'mesh2D'
    vel_2d.standard_name = 'sea_water_speed'
    vel_2d.units = 'm s-1'
    vel_2d[0, :] = np.linspace(2., 6., edges_2d)
    vel_2d[1, :] = np.linspace(6., 2., edges_2d)

    # global attributes
    ncfile.Conventions = "CF-1.8 UGRID-1.0 Deltares-0.9"
    ncfile.history = "Created on %s)" % datetime.now()
    ncfile.institution = "Deltares"
    ncfile.reference = "http://www.deltares.nl"
    ncfile.source = "Python script to test layout of a UGRID 2DH map file"

    return ncfile


if __name__ == "__main__":
    # main(nc_root, var_name)
    print("\n%s" % sys.version)

    start_time = datetime.now()
    print('Start: %s\n' % start_time)
    print('Create UGRID netCDF4 file (2DH)')
    filename = Path(__file__).stem + '.nc'
    nc_file = netCDF4.Dataset(filename, "w", format="NETCDF4")
    print("%s" % nc_file.data_model)

    main(nc_file)
    print("%s" % nc_file.Conventions)
    nc_file.close()

    print('\nStart: %s' % start_time)
    print('End  : %s' % datetime.now())
    print('Klaar')
