import pyxdf

def read_xdf_markers(filename):
    # Load the XDF file
    data, header = pyxdf.load_xdf(filename)

    # Search for streams with marker information
    marker_streams = [stream for stream in data]

    for i in range(len(marker_streams)):
    # Retrieve the markers from the first marker stream
        print(i)
        markers = marker_streams[i]['time_series']
       # type = marker_streams[0]['time_series']
        timestamps = marker_streams[i]['time_stamps']

        # Print the marker data
        for ts, marker in zip(timestamps, markers):
            print(f"Type: Timestamp: {ts:.6f}, Marker: {marker[0]}")

if __name__ == "__main__":
    # Replace 'your_xdf_file.xdf' with the actual file path
    xdf_file_path = 'recorded_lsl.xdf'
    read_xdf_markers(xdf_file_path)
