def can_insert_ads(feed_items, n):
    count = 0
    for i in range(-1, len(feed_items)):
        '''
        Check if current position has valid left 
        and right elements for placing an ad
        '''
        left_is_normal = i == -1 or feed_items[i] == 0
        right_is_normal = i == len(feed_items) - 1 or feed_items[i + 1] == 0
        
        if left_is_normal and right_is_normal:
            count += 1
            # Return early if we’ve found enough spots
            if count >= n:
                return True 

    if count >= n:
        return True
    else:
        return False