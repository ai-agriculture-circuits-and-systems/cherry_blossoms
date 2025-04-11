 # Cherry Blossoms Dataset

A historical phenological dataset tracking cherry tree flowering dates in Kyoto, Japan, from the 9th century to the present day. This dataset provides valuable insights into climate change and seasonal patterns over centuries.

## Dataset Description

The dataset contains historical records of cherry blossom flowering dates (sakura) in Kyoto, Japan, along with associated temperature data. The records span over 1200 years, making it one of the longest continuous phenological records in the world.

### Data Sources

- Historical records from the 9th to 14th centuries were collected by Aono and Saito (2010)
- Records from the 15th to 21st centuries were collected by Aono and Kazui (2008)
- All dates are converted to the Gregorian calendar for consistency

### Features

- `year`: Year in Common Era (CE)
- `doy`: Day of year for first bloom (e.g., Day 89 is April 1, Day 119 is May 1)
- `temp`: March temperature estimate
- `temp_upper`: Upper 95% confidence bound for temperature estimate
- `temp_lower`: Lower 95% confidence bound for temperature estimate

### Dataset Statistics

- Total number of records: 1,216
- Time span: 9th century to present
- Download size: 26.90 KiB
- Dataset size: 119.84 KiB

## Citation

If you use this dataset in your research, please cite:

```
@ONLINE {
    author = "Aono, Yasuyuki",
    title  = "Historical Series of Phenological data for Cherry Tree Flowering at Kyoto City (and March Mean Temperature Reconstructions)",
    year   = "2012",
    url    = "http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/"
}
```

## License

This dataset is available under the Creative Commons Attribution 4.0 License. See the [LICENSE](LICENSE) file for details.

## Usage

For detailed information about using this dataset, please refer to the [USAGE.md](USAGE.md) file.

## Acknowledgments

- Original data collection and research by Yasuyuki Aono and colleagues
- Data hosted and maintained by TensorFlow Datasets
- Temperature reconstructions based on historical records and modern measurements