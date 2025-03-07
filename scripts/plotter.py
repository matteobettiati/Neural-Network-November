import matplotlib.pyplot as plt
import numpy as np

def plot_distribution(*datas):
    """
    Graphs are plotted horizontally.
    One or many label sets can be passed as arguments.
    Usage:
    - `plot_distribution(data['labels'])`
    - `plot_distribution(data_labels, augmented_labels)`
    """
    n = len(datas)
    fig, axes = plt.subplots(1, n, figsize=(n * 5, 5))
    if n == 1:
        axes = [axes]
    for ax, data in zip(axes, datas):
        classes = len(np.unique(data))
        counts = np.bincount(data.flatten(), minlength=classes)
        bars = ax.bar(range(classes), counts, tick_label=[i for i in range(classes)])
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, str(int(yval)), ha='center', va='bottom')
        ax.set_ylabel("Count")
        ax.set_xlabel("Label")
        ax.set_xticklabels([i for i in range(classes)])
    plt.tight_layout()
    plt.show()

def plot_image(*images):
    """
    Images are plotted horizontally.
    One or many images can be passed as arguments.
    Usage:
    - `plot_image(image)`
    - `plot_image(image, augmented_image)`
    """
    n = len(images)
    fig, axes = plt.subplots(1, n, figsize=(n * 3, 3))
    if n == 1:
        axes = [axes]
    for ax, image in zip(axes, images):
        ax.imshow(image)
        ax.axis('off')
    plt.show()

def plot_images(images, labels, row=8):
    """
    Initial images and final images of each label are
    plotted horizontally.
    Usage:
    - `plot_images(images, labels)`
    - `plot_images(images, labels, row=8)`
    """
    classes = len(np.unique(labels))
    for i in range(classes):
        print(f"Class: {i+1}/{classes}")
        indices = np.where(labels == i)[0]
        plot_image(*images[indices[:row]])
        plot_image(*images[indices[-row:]])

def plot_masked_image(*images, mask_unique=4, mask_alpha=0.25):
    """
    Images are plotted horizontally.
    Images and masks are passed together as a tuple.
    Masks are dimmed to 0.5 and applied over the image.
    One or many images can be passed as arguments.
    Usage:
    - `plot_masked_image((image, mask))`
    - `plot_masked_image((image, mask), (aug_image, aug_mask))`

    The parameter `mask_unique` is used to set the
    number of values on which the mask pixels are
    normalized on (e.g. mask_unique=4).

    The parameter `mask_alpha` is used to set the
    alpha value of the mask, which is applied on
    the image (e.g. mask_alpha=0.25).
    """
    n = len(images)
    fig, axes = plt.subplots(1, n, figsize=(n * 4, 4))
    if n == 1:
        axes = [axes]
    for ax, pair in zip(axes, images):
        image, mask = pair
        image = (image - np.min(image)) / (np.max(image) - np.min(image))
        normalized_mask = mask / mask_unique
        blended_image = image * (1-mask_alpha) + normalized_mask * mask_alpha
        ax.imshow(blended_image, cmap='gray')
        ax.imshow(normalized_mask, cmap='viridis', alpha=mask_alpha)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def plot_masked_images(images, masks, row=4):
    """
    Initial images and final images of the dataset are
    plotted horizontally, with masks applied to the
    image with same index.
    Usage:
    - `plot_masked_images(images, labels)`
    - `plot_masked_images(images, labels, row=4)`
    """
    last = len(images)
    first_images = [(images[i], masks[i]) for i in range(row)]
    last_images = [(images[i], masks[i]) for i in range(last - row, last)]
    plot_masked_image(*first_images)
    plot_masked_image(*last_images)
